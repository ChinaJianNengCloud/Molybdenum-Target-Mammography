import cv2
import os
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# 输入和输出路径
filepath = r'M:\sjwlab\meixuewen\onelocalimages_view_cro'
fileoutpath = r'M:\sjwlab\meixuewen\zstack\max'
os.makedirs(fileoutpath, exist_ok=True)

# 定义处理函数
def gjjmax(imagefilepath, output_path):
    # 初始化最大图像为第一张图像
    path1 = os.path.join(imagefilepath, os.listdir(imagefilepath)[0])
    imbase = cv2.imread(path1, 0)
    height, width = imbase.shape
    max_image = np.zeros_like(imbase)

    # 遍历文件夹中的所有图像
    for image in os.listdir(imagefilepath):
        path = os.path.join(imagefilepath, image)
        im = cv2.imread(path, 0)
        im = cv2.resize(im, (width, height), interpolation=cv2.INTER_AREA)

        # 在每个位置上比较像素值，选出最大值
        max_image = np.maximum(max_image, im)

    # 保存最大值图像
    cv2.imwrite(output_path, max_image)

# 创建一个线程池
with ThreadPoolExecutor(max_workers=32) as executor:  # 可以根据实际情况调整 max_workers 的大小
    # 遍历文件夹
    for idfile in os.listdir(filepath):
        id_path = os.path.join(filepath, idfile)
        idout_path = os.path.join(fileoutpath, idfile)
        os.makedirs(idout_path, exist_ok=True)
        for viewfile in os.listdir(id_path):
            view_path = os.path.join(id_path, viewfile)
            viewout = os.path.join(idout_path, viewfile + '.png')
            # 提交任务到线程池
            executor.submit(gjjmax, view_path, viewout)

print("所有任务已完成。")
