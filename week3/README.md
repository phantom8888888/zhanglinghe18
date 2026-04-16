# zhanglinghe18
让小乌龟（Turtlesim）在 Ubuntu 中画圆，最直观的方法是通过 速度控制（Velocity Control）。

在 ROS 中，画圆的逻辑很简单：同时给小乌龟一个恒定的“线速度”（前进）和一个恒定的“角速度”（转弯）。

方法一：使用命令行（最简单、无需写代码）
如果你已经安装并启动了 roscore 和 turtlesim_node，直接在新的终端输入以下命令：

对于 ROS 1 (Noetic/Melodic):
Bash
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist "linear:
  x: 2.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 1.0" -r 10
对于 ROS 2 (Foxy/Humble/Jazzy):
Bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}"
参数解释：

linear x: 2.0：代表每秒前进 2 个单位。

angular z: 1.0：代表每秒旋转 1 个弧度。

-r 10：代表以每秒 10 次的频率重复发送指令（如果不加这个，乌龟动一下就停了）。

方法二：编写 Python 脚本控制
如果你想通过程序控制，可以创建一个 Python 文件（例如 draw_circle.py）。这里以 ROS 1 为例：

Python
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def rotate_turtle():
    # 1. 初始化节点
    rospy.init_node('turtle_circle_node', anonymous=True)
    
    # 2. 创建发布者，发布到 cmd_vel 话题
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    vel_msg = Twist()
    
    # 3. 设置速度数值
    vel_msg.linear.x = 2.0  # 前进速度
    vel_msg.angular.z = 1.0 # 旋转速度
    
    rate = rospy.Rate(10) # 10Hz

    while not rospy.is_shutdown():
        # 4. 循环发布消息
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        rotate_turtle()
    except rospy.ROSInterruptException:
        pass
运行步骤：

保存代码后，给文件权限：chmod +x draw_circle.py

运行它：python3 draw_circle.py
Shinhan University | International College | Software Major 🇰🇷 소개 (Introduction) 본 저장소는 신한대학교 국제대학 소프트웨어전공의 'AI 로봇공학' 강의 과제를 기록하고 관리하는 공간입니다. 기초적인 로봇 운동학(Kinematics)부터 **ROS(Robot Operating System)**를 이용한 고차원 제어, 그리고 인공지능을 결합한 지능형 로봇 시스템 구축을 목표로 합니다.

성명: 장 창

주요 학습 내용: PyBullet 시뮬레이션, 정/역운동학, ROS 통신, 센서 데이터 처리, AI 기반 로봇 제어.

🇨🇳 简介 (Introduction) 本仓库用于存放和管理信韩大学国际大学软件专业“AI机器人”课程的相关作业。课程内容涵盖了从基础的机器人运动学（Kinematics）到使用 ROS (机器人操作系统) 进行的高阶控制，以及结合人工智能（AI）实现智能化机器人系统的构建。

姓名： 张畅

核心模块： PyBullet 仿真、正向/逆向运动学、ROS 通讯机制、传感器数据处理、基于 AI 的机器人控制。

🇺🇸 English (Introduction) This repository is dedicated to the assignments and projects of the AI Robotics course at Shinhan University (International College, Software Major). The curriculum spans from basic Robot Kinematics to advanced control using ROS (Robot Operating System), aiming to build intelligent robotic systems integrated with Artificial Intelligence.

Name: ZHANG CHANG
Key Topics: PyBullet Simulation, Forward/Inverse Kinematics, ROS Middleware, Sensor Data Processing, AI-driven Robot Control.

<img src="img/img1.png" alt="ros2 小乌龟" width="500">
<img src="img/img2.png" alt="机器狗" width="500">

README.md
