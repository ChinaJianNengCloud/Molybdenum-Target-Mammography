import os

import cv2
import numpy as np
from PIL import Image

# def resize_image(img, output_size=(600, 800)):
#
#     if img is None:
#         raise ValueError("无法读取图像或路径不正确")
#
#     width, height = output_size
#     resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
#
#     return resized_img
#
#
# def set_image_borders_to_black(img):
#     # # 读取图像
#     # img = cv2.imread(image_path)
#
#     # 获取图像的宽度和高度
#     height, width, channels = img.shape
#
#     # 设置左右两边20个像素为全黑
#     img[:, :35] = 0
#     img[:, width - 35:] = 0
#
#     # 设置上下两边10个像素为全黑
#     img[:10, :] = 0
#     img[height - 10:, :] = 0
#     return img
#
# # 示例使用
# input_path = r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\one\resize_redeal\org\all_images_de\A_0061_1.LEFT_CC.png'
# output_path = 'path_to_output_image.jpg'
#
# # 读取图像
# image = cv2.imread(input_path)
# if image is None:
#     raise ValueError("无法读取图像，请检查路径是否正确。")
#
# # 添加黑色边框
# image_with_borders = set_image_borders_to_black(image)
#
# # 显示结果
# cv2.imshow('Image with borders', resize_image(image_with_borders))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # 保存结果
# cv2.imwrite(output_path, image_with_borders)


##批量化
def set_image_borders_to_black(img):
    # # 读取图像
    # img = cv2.imread(image_path)

    # 获取图像的宽度和高度
    height, width, channels = img.shape

    # 设置左右两边20个像素为全黑
    img[:, :100] = 0
    img[:, width - 100:] = 0

    # 设置上下两边10个像素为全黑
    img[:15, :] = 0
    img[height - 15:, :] = 0
    return img
in_path=r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\one\resize_redeal\org\all_images_de'
out_path=r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\one\resize_redeal\org\all_images_de_blackborders'

os.makedirs(out_path,exist_ok=True)

for imagefile in os.listdir(in_path):
    imgaepath=os.path.join(in_path,imagefile)
    out=os.path.join(out_path,imagefile)
    img=cv2.imread(imgaepath)
    imgblackadd=set_image_borders_to_black(img)
    cv2.imwrite(out,imgblackadd)

