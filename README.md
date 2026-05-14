# zhanglinghe18

# AI 机器人课程作业

本仓库整理了 AI Robotics 课程的每周作业和实验笔记。

## 课程作业目录

- [Week 2：WSL、Ubuntu 与 ROS2 环境配置](week2/)
# Week 2：WSL、Ubuntu 与 ROS2 环境配置

## 实验内容

本周完成了以下任务：

1. 安装 WSL Ubuntu 22.04
2. 配置 ROS2 Humble 环境
3. 运行 turtlesim 小乌龟节点

## 实验截图

### Ubuntu 安装成功

<img src="img/ubuntu-install.png" alt="Ubuntu 安装" width="600">

### 小乌龟仿真运行

<img src="img/turtlesim.png" alt="小乌龟" width="600">

## 运行命令

\`\`\`bash
# 启动小乌龟节点
ros2 run turtlesim turtlesim_node

# 启动键盘控制
ros2 run turtlesim turtle_teleop_key
\`\`\`

## 遇到的问题

1. **问题**：运行 `ros2` 命令提示 command not found
   **解决**：运行 `source /opt/ros/humble/setup.bash`

- [Week 3：GitHub SSH、VS Code 与 ROS2 交互](week3/)
- [Week 4：命令行、机器人基础与 Python 仿真](week4/)
- [Week 5：Linux 目录操作与机器人运动学](week5/)
- [Week 6：传感器介绍与 ROS2 KITTI 实验](week6/)
- [Week 7：Markdown 与 GitHub 作业整理](week7/)
- [Week 8：Docker 安装与 ROS2 桌面容器](week8/)
- [Week 10：Docker 概念与 OpenCV 实验](week10/)

## 关于我

- 姓名：张畅
- 学号：20221926
- 专业：计算机科学与技术

## 项目说明

本项目使用 GitHub Pages 自动部署。

在线访问：[https://phantom8888888.github.io/zhanglinghe18/](https://你的用户名.github.io/仓库名/)
README.md
