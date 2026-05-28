"""
优化版 Laikago 四足机器狗 Trot 跑步程序
改进点：
  1. 初始状态直立站立（修正 URDF 默认朝向）
  2. 移除 resetBaseVelocity，纯关节力矩驱动真实跑步
  3. 髋关节 + 大腿协同驱动，提供真实推进力
  4. 缓慢站立过渡，避免弹飞
  5. 相机实时跟随
  6. 摔倒自动检测与重置
  7. GUI 滑块实时调整步态参数

运行：
    pip install pybullet numpy
    python laikago_trot_final.py
"""

import pybullet as p
import pybullet_data
import time
import math

# ============================================================
# 全局参数
# ============================================================
SIM_HZ     = 240                                        # 仿真频率 Hz
GRAVITY    = -9.8
ROBOT_URDF = "laikago/laikago_toes.urdf"
START_POS  = [0, 0, 0.52]                              # 初始位置（稍高于地面）

# laikago URDF 坐标系默认是趴下状态，绕 X 轴旋转 180° 修正为直立
START_ORI  = p.getQuaternionFromEuler([math.pi / 2, 0, math.pi / 2]) 

# 站立目标角度
STAND_UPPER = 0.75    # 大腿 (rad)
STAND_LOWER = -1.50   # 小腿 (rad)
STAND_FORCE = 80      # 站立力矩

# 关节最大力矩
JOINT_FORCE = 120

# Trot 步态默认参数（GUI 滑块初始值）
DEFAULT_FREQ        = 1.8   # 步频 Hz
DEFAULT_HIP_SWING   = 0.35  # 髋关节摆幅
DEFAULT_UPPER_SWING = 0.20  # 大腿摆幅
DEFAULT_KNEE_LIFT   = 0.40  # 抬腿幅度

# 摔倒判断
FALL_HEIGHT = 0.25   # 机身低于此高度判定为摔倒 (m)
FALL_ANGLE  = 1.0    # roll/pitch 超过此角度判定为摔倒 (rad)


# ============================================================
# 初始化
# ============================================================
def init_sim():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, GRAVITY)
    p.setTimeStep(1.0 / SIM_HZ)
    p.setRealTimeSimulation(0)
    p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)
    p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 1)
    p.resetDebugVisualizerCamera(
        cameraDistance=1.8,
        cameraYaw=45,
        cameraPitch=-25,
        cameraTargetPosition=[0, 0, 0.3],
    )


def load_scene():
    p.loadURDF("plane.urdf")


def load_robot():
    return p.loadURDF(
        ROBOT_URDF,
        basePosition=START_POS,
        baseOrientation=START_ORI,   # 直立站立
        flags=p.URDF_USE_SELF_COLLISION,
    )


# ============================================================
# 关节映射
# ============================================================
def get_legs(robot):
    joint_map = {}
    for j in range(p.getNumJoints(robot)):
        name = p.getJointInfo(robot, j)[1].decode("utf-8")
        joint_map[name] = j

    # FR+RL 同相（对角），FL+RR 反相
    legs = {
        "FR": {"hip": joint_map["FR_hip_motor_2_chassis_joint"],
               "upper": joint_map["FR_upper_leg_2_hip_motor_joint"],
               "lower": joint_map["FR_lower_leg_2_upper_leg_joint"],
               "phase": 0.0},
        "RL": {"hip": joint_map["RL_hip_motor_2_chassis_joint"],
               "upper": joint_map["RL_upper_leg_2_hip_motor_joint"],
               "lower": joint_map["RL_lower_leg_2_upper_leg_joint"],
               "phase": 0.0},
        "FL": {"hip": joint_map["FL_hip_motor_2_chassis_joint"],
               "upper": joint_map["FL_upper_leg_2_hip_motor_joint"],
               "lower": joint_map["FL_lower_leg_2_upper_leg_joint"],
               "phase": math.pi},
        "RR": {"hip": joint_map["RR_hip_motor_2_chassis_joint"],
               "upper": joint_map["RR_upper_leg_2_hip_motor_joint"],
               "lower": joint_map["RR_lower_leg_2_upper_leg_joint"],
               "phase": math.pi},
    }
    return legs


# ============================================================
# GUI 滑块
# ============================================================
def add_sliders():
    return {
        "freq":        p.addUserDebugParameter("步频 Hz",   0.5, 3.5, DEFAULT_FREQ),
        "hip_swing":   p.addUserDebugParameter("髋关节摆幅", 0.0, 0.6, DEFAULT_HIP_SWING),
        "upper_swing": p.addUserDebugParameter("大腿摆幅",   0.0, 0.5, DEFAULT_UPPER_SWING),
        "knee_lift":   p.addUserDebugParameter("抬腿幅度",   0.0, 0.8, DEFAULT_KNEE_LIFT),
    }


def read_sliders(sliders):
    return {k: p.readUserDebugParameter(v) for k, v in sliders.items()}


# ============================================================
# 关节控制
# ============================================================
def set_joint(robot, joint_id, target, force=JOINT_FORCE):
    p.setJointMotorControl2(
        robot, joint_id,
        p.POSITION_CONTROL,
        targetPosition=target,
        positionGain=0.4,
        velocityGain=0.05,
        force=force,
    )


# ============================================================
# 站立（缓慢线性插值，避免弹飞）
# ============================================================
def stand(robot, legs, steps=600):
    for s in range(steps):
        alpha = min(1.0, s / 400)
        for leg in legs.values():
            set_joint(robot, leg["hip"],   0.0,                 STAND_FORCE)
            set_joint(robot, leg["upper"], STAND_UPPER * alpha, STAND_FORCE)
            set_joint(robot, leg["lower"], STAND_LOWER * alpha, STAND_FORCE)
        p.stepSimulation()
        time.sleep(1.0 / SIM_HZ)


# ============================================================
# Trot 步态
# ============================================================
def trot_step(robot, legs, t, params):
    """
    对角步态（Trot）
    - upper (大腿)：用 cos 驱动，cos>0 前迈，cos<0 后蹬 → 产生推进力
    - lower (小腿)：摆动相抬起，支撑相伸直蹬地
    - hip  (髋关节)：微量侧摆保持平衡
    """
    freq        = params["freq"]
    hip_swing   = params["hip_swing"]
    upper_swing = params["upper_swing"]
    knee_lift   = params["knee_lift"]

    for leg in legs.values():
        phi = 2 * math.pi * freq * t + leg["phase"]

        sin_val       = math.sin(phi)
        cos_val       = math.cos(phi)
        swing_factor  = max(0.0,  sin_val)   # 摆动相因子 (0~1)
        stance_factor = max(0.0, -sin_val)   # 支撑相因子 (0~1)

        hip_target   = hip_swing * 0.05 * sin_val
        upper_target = STAND_UPPER + upper_swing * cos_val
        lower_target = STAND_LOWER - knee_lift * swing_factor + 0.15 * stance_factor

        set_joint(robot, leg["hip"],   hip_target)
        set_joint(robot, leg["upper"], upper_target)
        set_joint(robot, leg["lower"], lower_target)


# ============================================================
# 摔倒检测 & 重置
# ============================================================
def is_fallen(robot):
    pos, orn = p.getBasePositionAndOrientation(robot)
    roll, pitch, _ = p.getEulerFromQuaternion(orn)
    return pos[2] < FALL_HEIGHT or abs(roll) > FALL_ANGLE or abs(pitch) > FALL_ANGLE


def reset_robot(robot, legs):
    p.resetBasePositionAndOrientation(robot, START_POS, START_ORI)
    p.resetBaseVelocity(robot, [0, 0, 0], [0, 0, 0])
    for j in range(p.getNumJoints(robot)):
        p.resetJointState(robot, j, 0.0)
    stand(robot, legs, steps=400)


# ============================================================
# 相机跟随
# ============================================================
def update_camera(robot):
    pos, _ = p.getBasePositionAndOrientation(robot)
    p.resetDebugVisualizerCamera(
        cameraDistance=1.8,
        cameraYaw=45,
        cameraPitch=-25,
        cameraTargetPosition=[pos[0], pos[1], pos[2] + 0.1],
    )


# ============================================================
# 主程序
# ============================================================
def main():
    init_sim()
    load_scene()
    robot   = load_robot()
    legs    = get_legs(robot)
    sliders = add_sliders()

    print("[状态] 机器狗站立中，请稍候...")
    stand(robot, legs)

    print("[状态] 开始跑步！拖动右侧滑块可实时调整参数，Ctrl+C 退出。")

    t  = 0.0
    dt = 1.0 / SIM_HZ

    while True:
        params = read_sliders(sliders)

        trot_step(robot, legs, t, params)

        p.stepSimulation()
        t += dt

        if is_fallen(robot):
            print("[警告] 检测到摔倒，自动重置...")
            t = 0.0
            reset_robot(robot, legs)

        # 每 4 步更新一次相机，降低开销
        if int(t * SIM_HZ) % 4 == 0:
            update_camera(robot)

        time.sleep(dt)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[停止] 用户退出。")
        p.disconnect()