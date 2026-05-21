姓名：张畅 (zhangchang) 所属：信韩大学国际大学软件专业 (Shinhan University | International College | Software Major) 🇰🇷 课程：AI人工智能机器人 (AI Robotics)

🇨🇳 本次操作叙述 (Description of Activities)
本次实验主要完成了 Docker 容器环境下的 ROS2 图形化仿真部署，并进一步实现了 TurtleSim 小乌龟的键盘控制与交互测试。通过 Docker Desktop、noVNC、ROS2 以及 TurtleSim 的结合，成功验证了 ROS2 节点通信与容器化图形环境的运行效果。

1. Docker + ROS2 图形化环境搭建
实验内容
本次首先在 Windows PowerShell 中启动 ROS2 Desktop Docker 容器，并开启基于 VNC 的图形界面服务。

执行命令：

docker run -p 6080:80 --security-opt seccomp=unconfined --shm-size=512m ghcr.io/ti.../ros2-desktop-vnc:humble
成功启动 Ubuntu Jammy ROS2 Desktop 环境，并完成端口映射。

随后通过浏览器访问：

127.0.0.1:6080
进入 noVNC 提供的 Ubuntu 图形桌面，实现 Docker 容器内桌面的可视化操作。

实验结果
成功进入 Ubuntu 图形桌面
noVNC 与 VNC 服务均显示 RUNNING 状态
Docker Desktop 中成功显示运行中的 ROS2 容器
浏览器可正常访问远程桌面
2. ROS2 TurtleSim 仿真运行
实验内容
进入 Docker 容器终端后，执行以下命令启动 TurtleSim：

ros2 run turtlesim turtlesim_node
系统成功弹出 TurtleSim 仿真窗口，显示蓝色背景及位于中央的小乌龟。

终端中同时输出 TurtleSim 初始化日志，包括小乌龟生成坐标与节点启动信息。

实验结果
TurtleSim 图形界面成功启动
ROS2 图形节点运行正常
小乌龟生成位置初始化成功
容器内图形程序运行稳定
3. TurtleSim 键盘控制（Teleop）
实验内容
在新的终端窗口中运行：

ros2 run turtlesim turtle_teleop_key
启动 TurtleSim 键盘控制节点。

通过键盘方向键（↑ ↓ ← →）控制小乌龟移动，并使用其他旋转控制键调整运动方向。

在控制过程中，小乌龟成功绘制出连续运动轨迹，说明速度控制话题 /cmd_vel 已被正确发布与接收。

终端显示：

Reading from keyboard
表明 teleop 节点已经进入实时监听状态。

实验结果
成功实现键盘控制
小乌龟能够自由移动与旋转
TurtleSim 中成功生成运动轨迹
验证 ROS2 Topic 通信机制正常工作
4. Docker Desktop 管理与监控
实验内容
通过 Docker Desktop 对容器运行状态进行监控。

界面中能够查看：

容器运行状态
镜像信息
端口映射情况
CPU 与内存资源占用
同时完成 Docker 镜像 commit 操作，用于保存当前实验环境。

实验结果
Docker 容器运行稳定
ROS2 图形环境可持续运行
镜像保存成功
开发环境具备良好的可复现性
🇺🇸 English Summary
Docker + ROS2 Environment
A ROS2 Desktop container with VNC support was launched using Docker. The Ubuntu graphical desktop was accessed through noVNC via browser at localhost:6080. Both VNC and noVNC services were verified to be running correctly.

TurtleSim Simulation
The command below was executed:

ros2 run turtlesim turtlesim_node
The TurtleSim GUI window launched successfully with a turtle displayed in the center. Initialization logs confirmed successful ROS2 node startup.

Keyboard Control (Teleop)
The teleoperation node was launched using:

ros2 run turtlesim turtle_teleop_key
Arrow keys were used to control the turtle movement and generate trajectories inside the simulator. This verified successful ROS2 topic communication.

Docker Management
Docker Desktop was used to monitor container status, resource usage, and port mappings. The ROS2 container environment operated stably throughout the experiment.

🇰🇷 한국어 요약
Docker 및 ROS2 환경 구성
Docker를 사용하여 ROS2 Desktop 컨테이너를 실행하고 noVNC 기반 GUI 환경을 구축하였다. 브라우저(127.0.0.1:6080)를 통해 Ubuntu 데스크탑 환경에 접속하였다. VNC 및 noVNC 서비스가 정상적으로 실행됨을 확인하였다.

TurtleSim 시뮬레이션
다음 명령어를 실행하여 TurtleSim을 구동하였다.

ros2 run turtlesim turtlesim_node
파란 배경의 TurtleSim GUI 창이 정상적으로 실행되었으며 중앙에 거북이가 생성되었다.

키보드 제어 (Teleop)
다음 명령어를 통해 키보드 제어 노드를 실행하였다.

ros2 run turtlesim turtle_teleop_key
방향키를 이용하여 거북이를 이동시키고 다양한 이동 궤적을 생성하였다. 이를 통해 ROS2 노드 간 Topic 통신이 정상적으로 동작함을 확인하였다.

Docker 관리
Docker Desktop을 통해 컨테이너 상태 및 자원 사용량을 모니터링하였다. ROS2 기반 개발 환경이 안정적으로 실행됨을 확인하였다.

📸 实验过程截图说明
图 1：Docker 环境与 OpenCV 安装
docker opencv 安装

说明： 在 Docker ROS2 容器中使用 pip 安装 pybullet、opencv-python 与 opencv-contrib-python 等依赖库，并完成 numpy 相关环境配置。

图 2：Docker Desktop 与容器启动
docker ros2 desktop

说明： Docker Desktop 中显示 ROS2 Desktop 容器运行状态，PowerShell 输出 VNC 与 noVNC 服务启动日志，并成功映射 6080:80 端口。

图 3：GitHub Pages 首页部署结果
github pages

说明： 成功将 AI Robotics 课程实验内容部署至 GitHub Pages，实现课程作业在线展示。

图 4：Docker 容器运行与 TurtleSim 测试
docker turtlesim

说明： 在 Docker 容器环境中成功运行 TurtleSim，并完成 ROS2 图形仿真测试与键盘控制。

Docker 进阶指令。
Docker 镜像更新与保存。
GitHub Pages 网页部署完整指引。
轮式机器人介绍。