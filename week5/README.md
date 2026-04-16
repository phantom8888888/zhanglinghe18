# zhanglinghe18
1. 环境准备 (Workspace Setup)
首先，你需要有一个 ROS 2 工作空间（看你的路径是 ~/ros2_ws）。

Bash
# 创建工作空间
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
2. 下载 KITTI 发布器源代码
从图中背景的 GitHub 页面可以看到，你需要克隆特定的分支（ubuntu24 对应的是较新的 ROS 2 版本）：

Bash
git clone -b ubuntu24 https://github.com/ai-robot-class/ros2_kitti_publishers.git
3. 安装依赖与编译
在工作空间根目录下，使用 rosdep 安装缺少的依赖包，然后进行编译：

Bash
cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
colcon build --symlink-install
source install/setup.bash
4. 下载并配置数据集
你需要下载 KITTI 数据集（通常是图片序列和点云二进制文件），并将其放置在代码指定的路径下。

注意： 检查 ros2_kitti_publishers 中的配置文件或 Launch 文件，确保 dataset_path 指向你存放数据的文件夹。

5. 启动程序
你需要分步启动数据发布器和可视化工具：

启动数据发布器：

Bash
ros2 launch kitti_nbv_provider kitti_publisher.launch.py
启动 RViz2 可视化（显示点云）：

Bash
rviz2 -d src/ros2_kitti_publishers/rviz/default.rviz
启动 rqt 图像查看器：

Bash
rqt
# 在 rqt 插件菜单中选择 Visualization -> Image View，并订阅对应的相机话题
README.md
