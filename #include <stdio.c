# 第一行非常重要，确保图片能直接在网页显示
%matplotlib inline

import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. 尝试读取图片 (如果你已经上传了 cat.jpg)
img = cv2.imread('cat.jpg')

# 2. 如果没有图片，我们手动生成一个彩色方块来测试 OpenCV 是否正常
if img is None:
    print("未检测到 cat.jpg，正在生成测试图像...")
    img = np.zeros((300, 500, 3), np.uint8)
    cv2.putText(img, 'OpenCV is Working!', (50, 150), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# 3. 关键步骤：BGR 转 RGB
# 别忘了 OpenCV 读进来是 BGR，直接画颜色会错
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 4. 显示结果
plt.figure(figsize=(8, 5))
plt.imshow(img_rgb)
plt.axis('off') # 隐藏坐标轴
plt.show()