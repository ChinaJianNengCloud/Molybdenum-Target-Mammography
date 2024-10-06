import os
from pydicom import dcmread
from PIL import Image
import numpy as np

def convert_dcm_to_png(dcm_file_path, png_file_path):
    ds = dcmread(dcm_file_path)
    img = ds.pixel_array

    # 检查维度
    if len(img.shape) == 3:
        # 如果是三维数组，则选择第一帧作为输出
        img = img[0]

    # 将像素数据归一化到0-255范围
    img = (img - img.min()) * (255 / (img.max() - img.min()))
    img = Image.fromarray(img.astype('uint8'), 'L')
    img.save(png_file_path)
    print(f"Converted {dcm_file_path} to {png_file_path}")

# 使用方法
dcm_file_path = r'D:\sjwlab\meixuewen\all_data\our_data\dbt\org\train\manifest-1617905855234\Breast-Cancer-Screening-DBT\DBT-P00003\01-01-2000-DBT-S01306-MAMMO screening digital bilateral-33603\18379.000000-NA-61347\1-1.dcm'
png_file_path = 'png_file.png'
convert_dcm_to_png(dcm_file_path, png_file_path)