#同时将png文件转jpg（meixwaddnote）
# import cv2
# import numpy as np
# import os
#
# def preprocess_image_for_resnet(image_path):
#     image = cv2.imread(image_path)
#     if len(image.shape) == 2 or image.shape[2] == 1:
#         image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
#     elif image.shape[2] == 4:
#         image = image[:, :, :3]
#     return image
#
#
# image_path = 'D:\wuwei\Meixw\cbis_chi_duo_Benign'
# for filename in os.listdir(image_path):
#     if filename.endswith('.jpg') or filename.endswith('.png'):
#         path=os.path.join(image_path,filename)
#         preprocessed_image = preprocess_image_for_resnet(image_path)
#         cv2.imwrite(path,preprocessed_image)



# from PIL import Image
# import os
# import glob
#
# input_folder = r'D:\wuwei\Meixw\fimages\images_train'
# output_folder = r'D:\wuwei\Meixw\fimages\processed_images_train'
#
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
#
# png_files = glob.glob(os.path.join(input_folder, '*.png'))
#
# for file in png_files:
#     img = Image.open(file)
#     file_name = os.path.splitext(os.path.basename(file))[0]
#     new_file_path = os.path.join(output_folder, f"{file_name}.jpg")
#     img = img.convert('RGB')  # 确保图片是RGB格式，因为JPG不支持透明度
#     img.save(new_file_path, 'JPEG')
#
# print("所有PNG文件已转换为JPG。")

########gpt辅助多线程化

from PIL import Image
import os
import glob
from concurrent.futures import ThreadPoolExecutor

# 设置文件夹路径
input_folder = r'D:\wuwei\Meixw\fimages\images_val'
output_folder = r'D:\wuwei\Meixw\fimages\processed_images_val'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def convert_png_to_jpg(png_file):
    img = Image.open(png_file)
    file_name = os.path.splitext(os.path.basename(png_file))[0]
    new_file_path = os.path.join(output_folder, f"{file_name}.jpg")
    img = img.convert('RGB')  # 确保图片是RGB格式，因为JPG不支持透明度
    img.save(new_file_path, 'JPEG')

png_files = glob.glob(os.path.join(input_folder, '*.png'))

with ThreadPoolExecutor() as executor:
    # 提交所有图像转换任务到线程池
    for png_file in png_files:
        executor.submit(convert_png_to_jpg, png_file)

print("所有PNG文件已转换为JPG。")
