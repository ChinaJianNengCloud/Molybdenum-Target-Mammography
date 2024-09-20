# import os
# from pydicom import dcmread
# import cv2
# from PIL import Image
# import numpy as np
# import pydicom
# import os
# def black_pixel_ratio2(image_path, threshold=30):
#     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     height, width = img.shape
#
#     black_pixels = np.sum(img < threshold)
#
#     total_pixels = width * height
#     ratio = black_pixels / total_pixels if total_pixels > 0 else 0
#
#     return ratio, img
# def convert_dcm_to_png(dcm_file_path, png_file_path):
#     ds = dcmread(dcm_file_path)
#
#     img = ds.pixel_array
#
#     if len(img.shape) == 3:
#         # 如果是三维数组，则选择第一帧作为输出
#         img = img[0]
#
#     # 将像素数据归一化到0-255范围
#     img = (img - img.min()) * (255 / (img.max() - img.min()))
#     img = Image.fromarray(img.astype('uint8'), 'L')
#
#     img.save(png_file_path)
#     print(f"Converted {dcm_file_path} to {png_file_path}")
#
#     # 重新加载图像以计算像素平均值
#     img = Image.open(png_file_path)
#     img_data = img.getdata()
#     img_mean = sum(img_data) / len(img_data)
#
#     # 如果像素平均值大于127，则反转图像
#     if img_mean > 127:
#         img = Image.eval(img, lambda x: 255 - x)
#         img.save(png_file_path)
#         print(f"Image inverted and saved to {png_file_path}")
#
#
# org_path=r'D:\sjwlab\important_xinxikemuba'
# out_path=r'H:\sjwlab\meixuewen'
#
# os.makedirs(out_path,exist_ok=True)
#
# for idfile in os.listdir(org_path):
#     idpath=os.path.join(org_path,idfile)
#     idoutpath=os.path.join(out_path,idfile)
#     os.makedirs(idoutpath,exist_ok=True)
#     for dcmfile in os.listdir(idpath):
#         dcmpath=os.path.join(idpath,dcmfile)
#         dcmoutpath=os.path.join(idoutpath,dcmfile+'.png')
#         convert_dcm_to_png(dcmpath,dcmoutpath)



import os
from pydicom import dcmread
import cv2
from PIL import Image
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def black_pixel_ratio2(image_path, threshold=30):
    """
    计算给定灰度图像中黑色像素的比例。
    """
    # 使用OpenCV读取图像并转换为灰度图
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 计算图像大小
    height, width = img.shape

    # 使用NumPy计算黑色像素的数量
    black_pixels = np.sum(img < threshold)

    # 计算黑色像素的比例
    total_pixels = width * height
    ratio = black_pixels / total_pixels if total_pixels > 0 else 0

    return ratio, img

def convert_dcm_to_png(dcm_file_path, png_file_path):
    ds = dcmread(dcm_file_path)

    # 获取像素数据
    img = ds.pixel_array

    # 检查维度
    if len(img.shape) == 3:
        # 如果是三维数组，则选择第一帧作为输出
        img = img[0]

    # 将像素数据归一化到0-255范围
    img = (img - img.min()) * (255 / (img.max() - img.min()))

    # 创建PIL图像对象
    img = Image.fromarray(img.astype('uint8'), 'L')

    img.save(png_file_path)
    print(f"Converted {dcm_file_path} to {png_file_path}")

    # 重新加载图像以计算像素平均值
    img = Image.open(png_file_path)
    img_data = img.getdata()
    img_mean = sum(img_data) / len(img_data)

    # 如果像素平均值大于127，则反转图像
    if img_mean > 127:
        img = Image.eval(img, lambda x: 255 - x)
        img.save(png_file_path)
        print(f"Image inverted and saved to {png_file_path}")

def process_directory(idpath, idoutpath):
    for dcmfile in os.listdir(idpath):
        dcmpath = os.path.join(idpath, dcmfile)
        dcmoutpath = os.path.join(idoutpath, dcmfile + '.png')
        convert_dcm_to_png(dcmpath, dcmoutpath)

org_path = r'D:\sjwlab\important_xinxikemuba'
out_path = r'H:\sjwlab\meixuewen'

os.makedirs(out_path, exist_ok=True)

# 创建线程池
with ThreadPoolExecutor(max_workers=16) as executor:
    for idfile in os.listdir(org_path):
        idpath = os.path.join(org_path, idfile)
        idoutpath = os.path.join(out_path, idfile)
        os.makedirs(idoutpath, exist_ok=True)
        # 提交任务到线程池
        executor.submit(process_directory, idpath, idoutpath)