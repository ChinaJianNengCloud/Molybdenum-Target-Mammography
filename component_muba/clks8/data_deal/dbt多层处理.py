# import os
#
# import cv2
# from pydicom import dcmread
# from PIL import Image
# import numpy as np
#
# def convert_dcm_to_png(dcm_file_path, png_file_path):
#     # 读取.dcm文件
#     ds = dcmread(dcm_file_path)
#
#     # 获取像素数据
#     img = ds.pixel_array
#
#     # 检查维度
#     if len(img.shape) == 3:
#         # 如果是三维数组，则选择第一帧作为输出
#         img = img[0]
#
#     # 将像素数据归一化到0-255范围
#     img = (img - img.min()) * (255 / (img.max() - img.min()))
#
#     # 创建PIL图像对象
#     img = Image.fromarray(img.astype('uint8'), 'L')
#
#     # 保存为.png文件
#     img.save(png_file_path)
#     print(f"Converted {dcm_file_path} to {png_file_path}")
#
# # 使用方法
# dcm_file_path = r'D:\sjwlab\meixuewen\all_data\our_data\dbt\org\train\manifest-1617905855234\Breast-Cancer-Screening-DBT'
# png_file_path = r'D:\sjwlab\meixuewen\all_data\our_data\dbt\org\train\manifest-1617905855234\Breast-Cancer-Screening-DBT_png'
# #
# os.makedirs(png_file_path,exist_ok=True)
#
# for file1 in os.listdir(dcm_file_path):
#     path1=os.path.join(dcm_file_path,file1)
#     for file2 in os.listdir(path1):
#         path2=os.path.join(path1,file2)
#         for file3 in os.listdir(path2):
#             path3=os.path.join(path2,file3)
#             for file4 in os.listdir(path3):
#                 path4=os.path.join(path3,file4)
#                 print(path4)
#                 outpath=os.path.join(png_file_path,file1)
#                 os.makedirs(outpath,exist_ok=True)
#                 imout=os.path.join(outpath,file3+file4+'.png')
#                 convert_dcm_to_png(path4,imout)
#
#


#####多线程
import os
import cv2
from pydicom import dcmread
from PIL import Image
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def convert_dcm_to_png(dcm_file_path, png_file_path):
    # 读取.dcm文件
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

    # 保存为.png文件
    img.save(png_file_path)
    print(f"Converted {dcm_file_path} to {png_file_path}")

def collect_files(root_dir, output_dir):
    tasks = []
    for file1 in os.listdir(root_dir):
        path1 = os.path.join(root_dir, file1)
        outpath1 = os.path.join(output_dir, file1)
        os.makedirs(outpath1, exist_ok=True)
        for file2 in os.listdir(path1):
            path2 = os.path.join(path1, file2)
            for file3 in os.listdir(path2):
                path3 = os.path.join(path2, file3)
                for file4 in os.listdir(path3):
                    path4 = os.path.join(path3, file4)
                    if path4.endswith('.dcm'):
                        # 构建输出路径
                        imout = os.path.join(outpath1, f"{file3}_{file4}.png")
                        tasks.append((path4, imout))
    return tasks

if __name__ == "__main__":
    dcm_file_path = r'D:\sjwlab\meixuewen\all_data\our_data\dbt\org\train\manifest-1617905855234\Breast-Cancer-Screening-DBT'
    png_file_path = r'D:\sjwlab\meixuewen\all_data\our_data\dbt\org\train\manifest-1617905855234\Breast-Cancer-Screening-DBT_png'

    os.makedirs(png_file_path, exist_ok=True)

    # 收集所有任务
    tasks = collect_files(dcm_file_path, png_file_path)

    # 使用线程池来异步处理任务
    with ThreadPoolExecutor(max_workers=8) as executor:  # 可以根据需要调整最大线程数
        futures = [executor.submit(convert_dcm_to_png, task[0], task[1]) for task in tasks]
        for future in futures:
            future.result()  # 这里等待所有任务完成
    print('Conversion completed.')