本项目基于 Python + PyBullet 物理引擎，实现了一个四足机器狗（Laikago）的动态仿真系统，并通过 Trot（对角小跑）步态控制，实现机器狗的稳定运动。

该系统主要包括：

机器人模型加载
物理环境搭建
关节控制
步态生成
电机驱动
动态仿真

项目目标是模拟真实四足机器人（如 Boston Dynamics Spot、Unitree Go2）的基础运动控制原理。

二、系统架构

整个系统由以下模块组成：

Python主程序
│
├── PyBullet物理引擎
│
├── 地面环境（plane.urdf）
│
├── 四足机器人模型（Laikago URDF）
│
├── 电机控制系统
│
├── Trot步态控制器
│
└── 实时仿真循环
三、核心技术
1. PyBullet 物理引擎

PyBullet 是一个机器人仿真平台，主要用于：

刚体动力学
关节控制
碰撞检测
机器人运动仿真

程序通过：

p.connect(p.GUI)

启动图形化仿真环境。

2. URDF 机器人模型

机器狗使用：

laikago/laikago_toes.urdf

模型。

URDF（Unified Robot Description Format）用于描述：

机器人结构
关节
连杆
惯性参数
电机

加载方式：

robot = p.loadURDF(
    "laikago/laikago_toes.urdf",
    [0, 0, 0.52]
)

其中：

[0,0,0.52]
表示机器人初始位置。
四、关节系统分析

机器狗共有四条腿：

腿部	含义
FR	Front Right（右前）
FL	Front Left（左前）
RR	Rear Right（右后）
RL	Rear Left（左后）

每条腿包含：

Hip Joint（髋关节）
Upper Leg（大腿）
Lower Leg（小腿）

程序通过：

p.getJointInfo()

读取所有关节信息。

然后建立：

joint_map

用于快速索引。

五、初始站立姿态

为了让机器人保持稳定，需要设置默认站立角度。

程序中：

STAND_UPPER = 0.75
STAND_LOWER = -1.5

表示：

关节	角度
大腿	0.75 rad
小腿	-1.5 rad

形成：

自然弯曲支撑姿态

类似真实机器狗的站立状态。

六、Trot 步态分析
1. Trot 步态定义

Trot（对角小跑）是四足机器人最经典的步态。

特点：

同步腿
FR + RL
FL + RR

即：

右前腿与左后腿同步
左前腿与右后腿同步

这样可以保持：

重心稳定
运动平衡
较高速度
七、步态生成原理

程序核心使用：

g(t)=sin(2πft+ϕ)

生成周期性步态。

其中：

参数	含义
f	步频
t	时间
ϕ	相位差
2. 相位控制

程序中：

if name in ["FR", "RL"]:
    phase = 0
else:
    phase = math.pi

实现：

两组对角腿相差180°

从而形成 Trot 步态。

八、电机控制系统

PyBullet 使用：

p.setJointMotorControl2()

控制关节。

控制模式：

p.POSITION_CONTROL

即：

位置控制模式

机器人会自动尝试达到目标角度。