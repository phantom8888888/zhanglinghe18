姓名：张畅 (zhangchang) 所属：信韩大学国际大学软件专业 (Shinhan University | International College | Software Major) 🇰🇷 课程：AI人工智能机器人 (AI Robotics)
12.1.7 学生视角的课堂操作顺序
这一节按下面顺序操作，不必一开始就展开服务端代码细节。

第一步：先把网络打通
在 WSL 中执行：

sudo service tailscaled start
tailscale status
tailscale ip -4
目标：

确认 Tailscale 已启动
记下 WSL 的 Tailscale IP
例如：

100.88.77.66
第二步：完成 SSH 学习测试
在 WSL 中确保 SSH 服务已经装好并启动：

sudo apt update
sudo apt install openssh-server -y
sudo service ssh start
ss -tlnp | grep :22
然后鼓励学生用手机上的 SSH 客户端测试连接：

ssh robot@100.88.77.66
这一小步的目的，是让学生先建立一个非常清楚的感受：

Tailscale 确实把手机和 WSL 放进了同一个网络
手机不仅能当摄像头，也能做远程终端
第三步：先安装本周需要的 Python 库
在运行相机桥接程序之前，先安装本周需要的依赖。

如果系统里还没有 pip3，先安装：

sudo apt update
sudo apt install python3-pip -y
然后安装本周起始代码依赖：

pip3 install -r week12_starters/requirements.txt
这一步完成后，再运行桥接程序。

如果直接运行程序时看到下面这类报错：

No module named 'flask'
通常就说明依赖还没有安装完成。

第四步：运行老师提供的相机接收脚本
接下来不要求学生先看懂服务端代码，而是先把脚本运行起来。

例如：

python3 week12_starters/camera_bridge.py
此时学生只需要知道两件事：

这个脚本会在 WSL 中启动一个网页服务
这个脚本会接收手机浏览器传回来的图像帧
至于 Flask、SocketIO、HTTPS、自签名证书这些实现细节，可以等链路跑通后再解释。

这一程序在实时实验阶段需要持续运行：

只要手机浏览器还在发送视频帧，WSL 端这个程序就不要关闭
关闭它之后，手机页面虽然还在，但后端已经没有程序接收图像
只有在结束本次实时实验，或者已经把需要的图片保存完毕后，才可以停止
本周课堂统一采用最简单的协调方式：

相机接收、图像显示、ArUco 检测写在同一个 Python 程序里
不再额外启动第二个 Python 程序去“再读一次摄像头”
这样可以避免多个程序同时争抢同一条实时视频流
运行顺序统一为：

先启动 week12_starters/camera_bridge.py
再让手机浏览器接入
程序持续接收最新一帧
在同一个程序内部直接完成显示和识别
第五步：用手机浏览器访问页面
在手机浏览器中打开：

https://100.88.77.66:5000
注意：

这里的地址是 WSL 的 Tailscale IP
不是校园网地址
也不是 192.168.x.x
如果端口不是 5000，就替换成实际端口。

第六步：允许浏览器使用摄像头
打开页面后，浏览器会请求摄像头权限。

学生此时要做的是：

允许浏览器访问摄像头
将后置摄像头对准 ArUco 或棋盘格
保持页面停留在前台
如果一切正常，此时 WSL 端应该已经能收到图像。

本节课的最小成功流程
学生先装依赖：

pip3 install -r week12_starters/requirements.txt
再启动程序：

python3 week12_starters/camera_bridge.py
手机浏览器打开：

https://<WSL的Tailscale_IP>:5000
成功标志是同时看到下面三件事：

手机本地画面
服务端处理结果
ArUco ID 6 被识别
12.1.8 推荐调试顺序
在这一步里，最常见的问题不是算法，而是链路没有打通。建议统一按下面顺序排查：

先查网络 -> 再查服务 -> 再查浏览器权限 -> 最后查代码
1. 先查网络
tailscale status
tailscale ip -4
ping <手机的Tailscale_IP>
目标：

看得到手机
WSL 和手机在同一个 Tailnet 中
2. 再查服务
确认老师提供的脚本是否真的启动了网页服务：

ss -tlnp | grep 5000
3. 再查手机浏览器
看这三件事：

页面能不能打开
摄像头权限有没有给
页面是否保持在前台
4. 最后再查代码
只有在网络、端口、权限都正常后，才去怀疑：

帧是否真的发出去了
Python 是否成功解码
OpenCV 是否成功显示
最常见的基础报错之一是：

No module named 'flask'
这通常不是程序逻辑问题，而是还没有先执行：

pip3 install -r week12_starters/requirements.txt
最推荐的课堂拆分验证法
把这一步拆成四个最小成功点：

手机能访问 WSL 页面
手机浏览器能成功打开摄像头
WSL 能收到一帧图像
OpenCV 能成功显示这一帧图像
12.1.9 OpenCV 测试手机视频流
这一小节要确认的是：

手机画面能够稳定出现在 WSL 的 OpenCV 窗口里。

这一部分可以分成两层理解：

学生层面
学生先安装依赖：

pip3 install -r week12_starters/requirements.txt
然后运行：

python3 week12_starters/camera_bridge.py
然后在手机浏览器中打开：

https://<WSL的Tailscale_IP>:5000
看到画面成功进入 WSL，就说明这一段链路已经打通。

进一步理解
等链路跑通之后，再向学生解释老师提供的接收端脚本在做什么。下面给一个极简的参考实现。思路是：

WSL 中起一个 HTTPS 页面
手机浏览器打开页面
页面调用摄像头
页面把 JPEG 帧通过 WebSocket 发回 Python
Python 用 OpenCV 解码并显示
import cv2
import numpy as np
from flask import Flask, render_template_string
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

HTML = """
<!doctype html>
<html>
<body>
  <h3>HTML5 Camera Bridge</h3>
  <video id="video" autoplay playsinline style="width: 90vw;"></video>
  <canvas id="canvas" style="display:none;"></canvas>
  <script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>
  <script>
    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    const socket = io();

    async function main() {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: {
          width: 1280,
          height: 720,
          facingMode: "environment"
        },
        audio: false
      });
      video.srcObject = stream;

      setInterval(() => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0);
        canvas.toBlob(async (blob) => {
          const arrayBuffer = await blob.arrayBuffer();
          socket.emit("video_frame", arrayBuffer);
        }, "image/jpeg", 0.8);
      }, 100);
    }

    main();
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@socketio.on("video_frame")
def handle_frame(image_bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if frame is not None:
        cv2.imshow("HTML5 Camera Test", frame)
        cv2.waitKey(1)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, ssl_context="adhoc")
运行后，手机浏览器访问：

https://<WSL的Tailscale_IP>:5000
首次访问时如果浏览器提示证书风险，可以指导学生点击“继续访问”，因为这里使用的是临时自签名证书。

12.1.10 手机摄像头实验前的铁律
做标定和测距之前，必须要求学生在手机浏览器侧尽量固定：

分辨率
对焦模式
推荐设置：

分辨率：1280x720 或 1920x1080
对焦：尽量锁定，不要自动来回跳
原因：

自动对焦会改变焦距

相机标定默认认为焦距是固定的
如果手机自动变焦，前面算出的内参矩阵会失效
动态分辨率会破坏像素坐标系

如果浏览器传回来的分辨率中途变化
角点位置和标定结果都不再对应
这一步是后面“测距是否准确”的前提。
