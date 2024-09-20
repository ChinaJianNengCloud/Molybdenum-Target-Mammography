# import os
# import cv2
# import numpy as np
# def split_and_calculate_black_pixels_ratio(img):
#     width = img.shape[1]
#     split_line = width // 2
#
#     left_half = img[:, :split_line]
#     right_half = img[:, split_line:]
#
#     def black_pixel_ratio(half_img):
#         mask = np.all(half_img == [0, 0, 0], axis=-1)
#         black_pixels = np.count_nonzero(mask)
#         total_pixels = half_img.size // 3  # 因为是三通道图像
#         ratio = black_pixels / total_pixels if total_pixels > 0 else 0
#         return ratio
#
#     left_ratio = black_pixel_ratio(left_half)
#     right_ratio = black_pixel_ratio(right_half)
#
#     if left_ratio > right_ratio:
#         flag = 'RIGHT'
#     elif left_ratio < right_ratio:
#         flag = 'LEFT'
#     return flag
#
#
# in_path='H:\sjwlab\meixwtest'
# out='H:\sjwlab\meixwtestlr'
# os.makedirs(out,exist_ok=True)
# for idfile in os.listdir(in_path):
#     idpath=os.path.join(in_path,idfile)
#     for imfile in os.listdir(idpath):
#         impath=os.path.join(idpath,imfile)
#         img=cv2.imread(impath)
#         img[img==255]=0
#         ff=split_and_calculate_black_pixels_ratio(img)
#         outidpath = os.path.join(out, idfile+ff)
#         os.makedirs(outidpath, exist_ok=True)
#         cv2.imwrite(os.path.join(outidpath,imfile),img)
#
#


import os
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def split_and_calculate_black_pixels_ratio(img):
    width = img.shape[1]
    split_line = width // 2

    left_half = img[:, :split_line]
    right_half = img[:, split_line:]

    def black_pixel_ratio(half_img):
        mask = np.all(half_img == [0, 0, 0], axis=-1)
        black_pixels = np.count_nonzero(mask)
        total_pixels = half_img.size // 3  # 因为是三通道图像
        ratio = black_pixels / total_pixels if total_pixels > 0 else 0
        return ratio

    left_ratio = black_pixel_ratio(left_half)
    right_ratio = black_pixel_ratio(right_half)

    if left_ratio > right_ratio:
        flag = 'RIGHT'
    elif left_ratio < right_ratio:
        flag = 'LEFT'
    return flag

def process_image(idfile, imfile):
    idpath = os.path.join(in_path, idfile)
    impath = os.path.join(idpath, imfile)
    img = cv2.imread(impath)
    img[img == 255] = 0
    ff = split_and_calculate_black_pixels_ratio(img)
    outidpath = os.path.join(out, idfile + ff)
    os.makedirs(outidpath, exist_ok=True)
    cv2.imwrite(os.path.join(outidpath, imfile), img)

in_path = r'H:\sjwlab\meixuewen\local_org'
out = r'H:\sjwlab\meixuewen\local_lr'
os.makedirs(out, exist_ok=True)

# 创建一个线程池，最大线程数为os.cpu_count()
with ThreadPoolExecutor(max_workers=48) as executor:
    for idfile in os.listdir(in_path):
        idpath = os.path.join(in_path, idfile)
        for imfile in os.listdir(idpath):
            # 提交任务到线程池
            executor.submit(process_image, idfile, imfile)
