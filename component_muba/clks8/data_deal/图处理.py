import os
from concurrent.futures import ThreadPoolExecutor
import cv2
import numpy as np
def resize_image(img, output_size=(600, 800)):

    if img is None:
        raise ValueError("无法读取图像或路径不正确")

    width, height = output_size
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    return resized_img

def crop_image(img, crop_size=200):
    if img is None:
        raise ValueError("无法读取图像或路径不正确")

    height, width = img.shape
    new_height = height - 2 * crop_size
    new_width = width - 2 * crop_size


    if new_height <= 0 or new_width <= 0:
        raise ValueError("裁剪尺寸过大，请选择一个较小的裁剪尺寸")

    cropped_img = img[crop_size:height - crop_size, crop_size:width - crop_size]

    return cropped_img

def keep_largest_white_contour(img):


    if img is None:
        raise ValueError("无法读取图像或路径不正确")

    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return img
    largest_contour = max(contours, key=cv2.contourArea)

    mask = np.zeros_like(img)

    cv2.drawContours(mask, [largest_contour], -1, 255, -1)
    result = cv2.bitwise_and(img, mask)

    return result

import cv2

def histogram_equalization(img):

    if img is None:
        raise ValueError("无法读取图像或路径不正确")
    equalized_img = cv2.equalizeHist(img)

    return equalized_img

# img=cv2.imread(r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\mini\reimg\A_0006_1.LEFT_MLO.jpg',0)
# # # print(img.shape[-1])
# # # if len(img.shape) == 2:
# # #     print("这是灰度图像，只有一个通道")
# # # else:
# # #     print("这不是灰度图像")
# #
# # img_cro=crop_image(img)
# # keim=keep_largest_white_contour(img_cro)
# # equ_im=histogram_equalization(img)
# img_cro=crop_image(img)
# equim = histogram_equalization(img_cro)
# keim=keep_largest_white_contour(equim)
# cv2.imshow('im',resize_image(keim))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# in_path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
# out_path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
#
# os.makedirs(out_path,exist_ok=True)
#
# for file in os.listdir(in_path):
#     im_path=os.path.join(in_path,file)
#     img=cv2.imread(im_path,0)
#     img_cro=crop_image(img)
#     # equim=histogram_equalization(img_cro)
#     keim=keep_largest_white_contour(img_cro)
#     cv2.imwrite(os.path.join(out_path,file),keim)





##多线程
def process_image(file, in_path, out_path):
    im_path = os.path.join(in_path, file)
    img = cv2.imread(im_path, 0)
    img_cro = crop_image(img)
    keim = keep_largest_white_contour(img_cro)
    out_file_path = os.path.join(out_path, file)
    cv2.imwrite(out_file_path, keim)

in_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
out_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'

os.makedirs(out_path, exist_ok=True)

# 获取所有文件名
files = os.listdir(in_path)

# 使用多线程处理文件
with ThreadPoolExecutor() as executor:
    executor.map(lambda file: process_image(file, in_path, out_path), files)