姓名：张畅 (zhangchang) 所属：信韩大学国际大学软件专业 (Shinhan University | International College | Software Major) 🇰🇷 课程：AI人工智能机器人 (AI Robotics)
第14周：手机遥控+火灾通信+仿真机器人迷宫探索
本周选择课程项目方向B：使用ROS2turtlesim作为二维机器人仿真对象，通过手机发送控制命令，让小乌龟在迷宫中完成手动遥控和自动探索。项目遵守课程要求的“单一常驻程序”原则：网页只负责发送命令，turtlesim_web_bridge.py同时负责WebSocket通信、ROS2速度发布、迷宫碰撞检测、终点判定和自动探索调度。

项目目标
手机网页可以控制乌龟前进、后退、左转、右转和停止。
电脑端桥接程序通过WebSocket接收网页命令，并发布/turtle1/cmd_vel。
迷宫边界和障碍物具有碰撞检测，乌龟撞墙时不会继续前进。
接入器explorer.py，在自动模式下使用 A* 路径规划终点。
网页端显示二维迷宫、乌龟位置、轨迹、当前模式和碰撞状态。
文件结构
Week14/
├── README.md
├── img14-1.jpg
├── turtlesim_auto.mp4
├── week14_turtlesim_single_report_concise_updated.pdf
└── turtlesim_remote/
    ├── turtlesim_web_bridge.py
    ├── explorer.py
    ├── maze.py
    ├── index.html
    └── requirements.txt
运行方式
第一个终端启动turtlesim：

source /opt/ros/humble/setup.bash
ros2 run turtlesim turtlesim_node
第二个终端启动网页桥接程序：

source /opt/ros/humble/setup.bash
cd Week14/turtlesim_remote
pip install -r requirements.txt
python3 turtlesim_web_bridge.py
浏览器或手机打开：

http://localhost:8080
如果使用手机控制，需要手机和电脑进入同一个Tailscale网络，再访问电脑的Tailscale IP地址加端口8080。

自动探索实现
maze.py生成6x6复杂迷宫，并提供障碍物、边界、起点、终点和格点邻接关系。explorer.py使用A*算法在格点图上规划从当前位置到终点的路径，然后把路径点转换为连续运动控制。turtlesim_web_bridge.py在自动模式下循环调用：

linear, angular = self.explorer.decide(self.get_state())
获得速度命令后仍然经过原有的compute_safe_motion()安全检查，因此自动模式和手动共享模式同一套碰撞检测与终点判定逻辑。

界面与结果
第14周海龟模拟迷宫项目

点击查看本周演示视频

项目还包含演示视频turtlesim_auto.mp4和报告week14_turtlesim_single_report_concise_updated.pdf。网页index.html支持手动/自动切换，自动运行时会在迷宫预测中对应行走轨迹，方便展示探索过程。

验证记录
已完成以下静态检查：

python -m py_compile turtlesim_remote/maze.py turtlesim_remote/explorer.py turtlesim_remote/turtlesim_web_bridge.py
python turtlesim_remote/maze.py
python turtlesim_remote/explorer.py
迷宫自检结果显示BFS有效，A*规划器能够生成到达终点的路径。

学习总结
这个项目把前面几周的内容串在一起：第 7 周的网页与仓库整理、第 10 周的 Python/OpenCV 工程习惯、第 12 周的手机与无线通信，以及 ROS2 的关注控制。最大的收获是理解了“控制货运必须集中”的工程原则。自动探索不是另外开一个程序抢控制，而是作为常驻桥程序内部的一个模式运行，这样接状态、重叠、终端和网页显示都保持一致。
