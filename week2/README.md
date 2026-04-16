# zhanglinghe18
在 Ubuntu 系统中，“小乌龟”通常指的是 ROS (Robot Operating System) 中的经典入门案例——Turtlesim。

要在 Ubuntu 上生成并控制这只小乌龟，请按照以下步骤操作：

1. 启动 ROS 核心 (Master)
打开第一个终端，输入以下命令启动 ROS 的基础服务：

Bash
roscore
注意：如果使用的是 ROS 2 (如 Foxy, Humble)，则跳过此步，直接从第 2 步开始。

2. 启动小乌龟窗口
打开第二个终端（不要关闭第一个），运行以下命令：

ROS 1 (Noetic/Melodic):

Bash
rosrun turtlesim turtlesim_node
ROS 2:

Bash
ros2 run turtlesim turtlesim_node
此时，你应该会看到一个蓝色背景的窗口，中间有一只静止的小乌龟。

3. 启动键盘控制节点
如果你想让小乌龟动起来，需要再打开第三个终端，运行控制节点：

ROS 1 (Noetic/Melodic):

Bash
rosrun turtlesim draw_square
(或者手动键盘控制：)

Bash
rosrun turtlesim turtle_teleop_key
ROS 2:

Bash
ros2 run turtlesim turtle_teleop_key
常见操作说明
如何移动： 在键盘控制终端激活的状态下，使用键盘上的方向键（上下左右）来控制乌龟的移动和转向。

如何生成多只乌龟（进阶）：
你可以通过调用服务（Service）在指定位置生成（spawn）新乌龟。例如在 ROS 1 中：

Bash
rosservice call /spawn "{x: 5.0, y: 5.0, theta: 0.0, name: 'turtle2'}"
README.md
