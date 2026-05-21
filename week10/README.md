课程作业记录与进度汇报
姓名： 张畅 (zhangchang) 所属： 信韩大学国际大学软件专业 (Shinhan University | International College | Software Major) 🇰🇷 课程： AI人工智能机器人 (AI Robotics)

🇨🇳 本次操作叙述 (Description of Activities)
本次主要进行了 Python 计算机视觉环境配置与 OpenCV 基础图像处理实验，重点解决了依赖库安装冲突问题，并成功实现了图像的色彩空间转换（BGR 转 RGB/GRAY），具体内容如下：

Python 环境与依赖库安装 依赖安装： 在 WSL (Ubuntu) 终端中使用 pip3 安装 opencv-python、opencv-contrib-python 和 matplotlib。 权限与冲突解决： 遇到 "externally managed environment" 提示，使用 --break-system-packages 参数强制安装。 遇到 numpy 版本冲突（scipy 需要旧版，而 opencv 需要新版），通过手动指定版本 pip install "numpy<2" 并卸载重装，解决了依赖不兼容的报错。 环境验证： 最终成功在 VS Code 中导入 cv2 和 matplotlib.pyplot 库。

OpenCV 图像读取与显示 代码实现： 编写 tupian.py 脚本，利用 cv2.imread() 读取名为 image.png 的风景图片。 色彩校正： 由于 OpenCV 默认使用 BGR 格式，而 Matplotlib 使用 RGB 格式，代码中使用 cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 进行转换。 结果验证： 如图 1 所示，成功弹出了 Matplotlib 窗口，显示了色彩正常的彩色风景图（木栈道与海景），证明图像读取与显示通道正确。

图像灰度化处理 处理逻辑： 使用 cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY) 将原图转换为灰度图。 显示适配： 为了在 Matplotlib 中正常显示单通道灰度图，将其再次转换为 RGB 格式（COLOR_GRAY2RGB）。 结果验证： 如图 2 所示，程序成功显示了该风景图的黑白（灰度）版本，完成了从彩色到灰度的像素处理实验。

🇺🇸 English Summary
Name: Wang Xinhao

Activity:

Python Environment Setup Installed opencv-python and matplotlib in the WSL environment. Resolved dependency conflicts regarding numpy versions and system package management flags (--break-system-packages) to ensure library compatibility.

Image Processing with OpenCV Developed a Python script (tupian.py) to load an image file (image.png). Addressed the color channel discrepancy between OpenCV (BGR) and Matplotlib (RGB) using color conversion functions.

Visualization Results Successfully displayed the original color image using plt.imshow. Applied grayscale conversion (COLOR_BGR2GRAY) and displayed the resulting monochrome image, verifying the pixel processing logic.

🇰🇷 한국어 요약
이름: 왕신호 (Wang Xinhao)

활동 내용:

파이썬 환경 구축 WSL 우분투 환경에 opencv-python 및 matplotlib 라이브러리를 설치했습니다. numpy 버전 충돌 및 시스템 패키지 관리 오류를 해결하며 개발 환경을 세팅했습니다.

OpenCV 기초 실습 tupian.py 스크립트를 작성하여 image.png 파일을 로드했습니다. OpenCV의 BGR 포맷과 Matplotlib의 RGB 포맷 차이를 cvtColor 함수를 통해 보정했습니다.

결과 확인 원본 컬러 이미지를 정상적으로 출력했습니다. 이미지를 그레이스케일(Grayscale)로 변환하는 코드를 실행하여, 흑백 이미지를 성공적으로 시각화했습니다.





image 镜像
只读的模板，包含了运行应用程序所需的所有文件、依赖项、配置、库和运行环境。可以将其理解为轻量级的、可执行的“安装包”，用于在 Docker 容器中运行代码，确保应用程序在不同环境中保持一致性。
核心特性：
只读模板： 镜像在运行后不会被改变。
分层结构： 基于联合文件系统（UnionFS），通过分层叠加生成最终的文件系统。
可移植性： “一次构建，随处运行”，可在任意安装了 Docker 的服务器上启动。 [1, 2, 3, 4, 5]
形象类比：
镜像 (Image) 就像是面向对象编程中的 类（Class） 或软件安装光盘（ISO 文件）。
容器 (Container) 则是类的 实例（Instance） 或运行中的安装程序。



container 容器
软件运行环境，一个基于沙盒隔离的可执行进程，运行在宿主机上，但不依赖独立操作系统。
与镜像关系： 容器是镜像的运行实例。镜像是只读的，容器是在镜像基础上增加了一个可读可写层。
生成老虎 彩色照片 和暗灰色照片