# zhanglinghe18

第一步：环境安装PyBullet 是一个非常轻量级的物理引擎，安装非常简单。打开终端执行：Bash# 确保你有 python3 和 pip
sudo apt update
sudo apt install python3-pip

# 安装 pybullet
pip install pybullet
第二步：编写生成机械臂的代码要实现截图中“桌子 + 机械臂”的效果，你可以创建一个 arm_sim.py 文件，核心逻辑如下：Pythonimport pybullet as p
import pybullet_data
import time

# 1. 连接物理引擎（GUI 模式）
physicsClient = p.connect(p.GUI)

# 2. 设置搜索路径（用于找到自带的机械臂模型）
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 3. 设置重力
p.setGravity(0, 0, -9.81)

# 4. 加载地面和桌子
planeId = p.loadURDF("plane.urdf")
tableId = p.loadURDF("table/table.urdf", basePosition=[0, 0, 0])

# 5. 加载机械臂 (以经典的 Franka Panda 为例)
# basePosition 设置在桌面上方一点
startPos = [0, 0, 0.65] 
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
armId = p.loadURDF("franka_panda/panda.urdf", startPos, startOrientation, useFixedBase=True)

# 6. 循环仿真
while True:
    p.stepSimulation()
    time.sleep(1./240.)
第三步：运行与调试在终端中运行该脚本：Bashpython3 arm_sim.py
核心步骤说明URDF 模型加载：机械臂的外形和物理属性是通过 URDF (Unified Robot Description Format) 文件定义的。PyBullet 自带了一些常用的模型（如截图中的 Panda）。坐标定位：桌子的高度通常在 $0.6$ 到 $0.7$ 米之间。机械臂加载时 useFixedBase=True 非常重要，否则机械臂会因为重力从桌子上掉下去。相机数据（截图左侧部分）：如果你想实现截图左侧那三个“Synthetic Camera”窗口（RGB、深度图、分割图），需要调用 p.getCameraImage() 函数。这是做机器视觉和深度学习训练的关键步骤。
Shinhan University | International College | Software Major 🇰🇷 소개 (Introduction) 본 저장소는 신한대학교 국제대학 소프트웨어전공의 'AI 로봇공학' 강의 과제를 기록하고 관리하는 공간입니다. 기초적인 로봇 운동학(Kinematics)부터 **ROS(Robot Operating System)**를 이용한 고차원 제어, 그리고 인공지능을 결합한 지능형 로봇 시스템 구축을 목표로 합니다.

성명: 장 창

주요 학습 내용: PyBullet 시뮬레이션, 정/역운동학, ROS 통신, 센서 데이터 처리, AI 기반 로봇 제어.

🇨🇳 简介 (Introduction) 本仓库用于存放和管理信韩大学国际大学软件专业“AI机器人”课程的相关作业。课程内容涵盖了从基础的机器人运动学（Kinematics）到使用 ROS (机器人操作系统) 进行的高阶控制，以及结合人工智能（AI）实现智能化机器人系统的构建。

姓名： 张畅

核心模块： PyBullet 仿真、正向/逆向运动学、ROS 通讯机制、传感器数据处理、基于 AI 的机器人控制。

🇺🇸 English (Introduction) This repository is dedicated to the assignments and projects of the AI Robotics course at Shinhan University (International College, Software Major). The curriculum spans from basic Robot Kinematics to advanced control using ROS (Robot Operating System), aiming to build intelligent robotic systems integrated with Artificial Intelligence.

Name: ZHANG CHANG
Key Topics: PyBullet Simulation, Forward/Inverse Kinematics, ROS Middleware, Sensor Data Processing, AI-driven Robot Control.


README.md
