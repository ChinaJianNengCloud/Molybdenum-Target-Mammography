# import os
#
# import cv2
# import numpy as np
# from scipy.ndimage import label, find_objects
#
#
# def keep_largest_black_region(image):
#     """
#     只保留图中最大连通的黑色区域，其他设置为白色。
#
#     :param image: numpy数组，代表灰度图像
#     :return: 处理后的图像
#     """
#     # 将黑色区域标记为1，白色区域标记为0
#     labeled_array, num_features = label(image == 0)
#
#     # 如果没有黑色区域，直接返回全白图像
#     if num_features == 0:
#         return np.ones_like(image) * 255
#
#     # 获取每个连通区域的大小
#     sizes = np.bincount(labeled_array.ravel())
#
#     # 排除背景（标记为0）
#     sizes[0] = 0
#
#     # 获取最大连通区域的标签
#     largest_label = np.argmax(sizes)
#
#     # 创建一个与原图像大小相同的白色图像
#     new_image = np.ones_like(image) * 255
#
#     # 将最大连通区域设置为黑色
#     new_image[labeled_array == largest_label] = 0
#
#     return new_image
# def keep_largest_white_region(image):
#     """
#     只保留图中最大连通的白色区域，其他设置为黑色。
#
#     :param image: numpy数组，代表灰度图像
#     :return: 处理后的图像
#     """
#     # 将白色区域标记为1，黑色区域标记为0
#     labeled_array, num_features = label(image == 255)
#
#     # 找到最大的连通区域
#     if num_features == 0:
#         # 没有白色区域
#         return image
#     else:
#         # 获取每个连通区域的大小
#         sizes = np.bincount(labeled_array.ravel())
#         # 排除背景（标记为0）
#         sizes[0] = 0
#         # 获取最大连通区域的标签
#         largest_label = np.argmax(sizes)
#
#         # 创建一个与原图像大小相同的黑色图像
#         new_image = np.zeros_like(image)
#         # 将最大连通区域设置为白色
#         new_image[labeled_array == largest_label] = 255
#
#         return new_image
#
# def resize_image(img, output_size=(600, 800)):
#
#     if img is None:
#         raise ValueError("无法读取图像或路径不正确")
#
#     width, height = output_size
#     resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
#
#     return resized_img
# #
# # path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\mini\mask\A_0002_1.LEFT_CC\2.png'
# # img=cv2.imread(path,0)
# # keim=keep_largest_white_region(img)
# # keim=keep_largest_black_region(keim)
# # reim=resize_image(keim)
# # cv2.imshow('im',reim)
# #
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\mini\maskbf'
#
# for file in os.listdir(path):
#     filepath=os.path.join(path,file)
#     print(file)
#     for imgone in os.listdir(filepath):
#         if imgone.endswith('.png'):
#             impath=os.path.join(filepath,imgone)
#             img=cv2.imread(impath,0)
#             keim=keep_largest_white_region(img)
#             keim=keep_largest_black_region(keim)
#             cv2.imwrite(impath,keim)



#多线程
import os
import cv2
import numpy as np
from scipy.ndimage import label
from concurrent.futures import ThreadPoolExecutor

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
def keep_largest_black_region(image):
    labeled_array, num_features = label(image == 0)
    if num_features == 0:
        return np.ones_like(image) * 255
    sizes = np.bincount(labeled_array.ravel())
    sizes[0] = 0

    largest_label = np.argmax(sizes)
    new_image = np.ones_like(image) * 255

    new_image[labeled_array == largest_label] = 0

    return new_image

def keep_largest_white_region(image):

    labeled_array, num_features = label(image == 255)

    if num_features == 0:
        return image
    else:
        sizes = np.bincount(labeled_array.ravel())
        sizes[0] = 0
        largest_label = np.argmax(sizes)

        new_image = np.zeros_like(image)
        # 将最大连通区域设置为白色
        new_image[labeled_array == largest_label] = 255

        return new_image

def process_image(impath):
    img = cv2.imread(impath, 0)
    img=crop_image(img)
    keim = keep_largest_white_region(img)
    keim = keep_largest_black_region(keim)
    cv2.imwrite(impath, keim)

def process_images_in_directory(directory_path):
    with ThreadPoolExecutor() as executor:
        # for file in os.listdir(directory_path):
            # filepath = os.path.join(directory_path, file)
            # if os.path.isdir(filepath):
                for imgone in os.listdir(directory_path):
                    if imgone.endswith('.tif'):
                        impath = os.path.join(directory_path, imgone)
                        executor.submit(process_image, impath)

path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\mini\all_images_redeal_de2'

process_images_in_directory(path)