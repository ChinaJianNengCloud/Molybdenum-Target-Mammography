from PIL import Image
import cv2
import os
from concurrent.futures import ThreadPoolExecutor

def black_pixel_ratio(image_path, threshold=30):
    """
    计算给定灰度图像中黑色像素的比例。
    ...
    """
    with Image.open(image_path).convert('L') as img:
        width, height = img.size
        black_count = 0

        for y in range(height):
            for x in range(width):
                pixel_value = img.getpixel((x, y))
                if pixel_value < threshold:
                    black_count += 1

        total_pixels = width * height
        ratio = black_count / total_pixels if total_pixels > 0 else 0

    return ratio

# n=1
# def process_image(image_path):
#     ratio, _ = black_pixel_ratio(image_path)
#     if ratio < 0.1:
#         print(image_path)
#         im = cv2.imread(image_path)
#         cv2.imwrite(image_path, 255 - im)
#
#
# in_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
#
# # 使用 ThreadPoolExecutor 来并发处理图像
# with ThreadPoolExecutor() as executor:
#     for image in os.listdir(in_path):
#         impath = os.path.join(in_path, image)
#         print(n)
#         n+=1
#         executor.submit(process_image, impath)
# print(black_pixel_ratio(r"D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images\CR1966408RIGHTrmlo.png"))

# in_path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
# n=1
# for file in os.listdir(in_path):
#     impath=os.path.join(in_path,file)
#     if black_pixel_ratio(impath)<0.1:
#         im=cv2.imread(impath,0)
#         cv2.imwrite(impath,255-im)
#         print(file)
#     print(n)
#     n+=1

from PIL import Image
import cv2
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


def black_pixel_ratio(image_path, threshold=30):

    with Image.open(image_path).convert('L') as img:
        width, height = img.size
        black_count = 0

        for y in range(height):
            for x in range(width):
                pixel_value = img.getpixel((x, y))

                if pixel_value < threshold:
                    black_count += 1

        total_pixels = width * height
        ratio = black_count / total_pixels if total_pixels > 0 else 0

    return ratio


def process_image(image_path):
    if black_pixel_ratio(image_path) < 0.1:
        print(os.path.basename(os.path.dirname(image_path)))
        print(os.path.basename(image_path))
        im = cv2.imread(image_path)
        inverted_im = 255 - im
        cv2.imwrite(image_path, inverted_im)


in_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
n=1
image_paths = []
# for file in os.listdir(in_path):
#     imfile = os.path.join(in_path, file)
for image in os.listdir(in_path):
        impath = os.path.join(in_path, image)
        image_paths.append(impath)

# 使用多线程处理图像
with ThreadPoolExecutor(max_workers=32) as executor:
    futures = [executor.submit(process_image, path) for path in image_paths]
    for future in as_completed(futures):
        print(n)
        n += 1
        # 这里可以添加额外的逻辑来处理每个完成的任务
        pass