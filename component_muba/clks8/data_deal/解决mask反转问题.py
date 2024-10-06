import os

import cv2
import numpy as np


# def is_uniform_gray(image):

#     if np.all(image == 0) or np.all(image == 255):
#         return True

#     unique_values = np.unique(image)
#     if len(unique_values) == 2 and (0 in unique_values and 255 in unique_values):
#         black连通区域 = np.sum(image == 0) == np.prod(image.shape)
#         white连通区域 = np.sum(image == 255) == np.prod(image.shape)
#         return black连通区域 or white连通区域

#     return 0
def is_white_pixel_ratio_greater_than_half(img):

    if img is None:
        raise ValueError("无法读取图像或路径不正确")

    white_pixels = cv2.countNonZero(img)
    total_pixels = img.size

    white_pixel_ratio = white_pixels / total_pixels

    return white_pixel_ratio

def crop_image(img, crop_size=100):
    if img is None:
        raise ValueError("无法读取图像或路径不正确")

    height, width = img.shape
    new_height = height - 2 * crop_size
    new_width = width - 2 * crop_size


    if new_height <= 0 or new_width <= 0:
        raise ValueError("裁剪尺寸过大，请选择一个较小的裁剪尺寸")

    cropped_img = img[crop_size:height - crop_size, crop_size:width - crop_size]

    return cropped_img
def calculate_white_pixel_ratio(img):

    if img is None:
        print("Image not found or failed to load.")
        return

    height, width = img.shape

    # 计算不同高度的位置
    two_thirds_height = int(height * (2 / 5))
    half_height = int(height * (1 / 2))
    one_eighth_height = int(height * (1 / 8))  # 修改这里

    # 提取这些位置的行
    row_two_thirds = img[two_thirds_height, :]
    row_half = img[half_height, :]
    row_one_eighth = img[one_eighth_height, :]  # 修改这里

    # 计算白色像素的数量
    white_two_thirds = np.sum(row_two_thirds == 255)
    white_half = np.sum(row_half == 255)
    white_one_eighth = np.sum(row_one_eighth == 255)  # 修改这里

    # 计算白色像素的比例
    ratio_two_thirds = white_two_thirds / width
    ratio_half = white_half / width
    ratio_one_eighth = white_one_eighth / width  # 修改这里

    return ratio_two_thirds, ratio_half, ratio_one_eighth

# img=cv2.imread(r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\mini\maskbf\A_0018_1.LEFT_MLO\1.png',0)
# print(is_white_pixel_ratio_greater_than_half(img))
# results = calculate_white_pixel_ratio(img)
# print(results)
#
in_path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\mini\maskbf'
out_path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\mini\mask_redeal'

os.makedirs(out_path,exist_ok=True)

for file in os.listdir(in_path):
    filepath=os.path.join(in_path,file)
    for imageone in os.listdir(filepath):
        if imageone.endswith('.png'):
            impath=os.path.join(filepath,imageone)
            im=cv2.imread(impath,0)
            results = calculate_white_pixel_ratio(im)
            if results[1]>results[0] and is_white_pixel_ratio_greater_than_half(im)>=0.3 and results[1]>results[2]:
                cv2.imwrite(os.path.join(out_path,file+'.png'),im)
