from PIL import Image
import cv2
import os
from concurrent.futures import ThreadPoolExecutor



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


# print(black_pixel_ratio(r"D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images\CR1930048LEFTlmlo.png"))

in_path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
out_path=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images_redeal'

os.makedirs(out_path,exist_ok=True)

for im in os.listdir(in_path):
    im_path=os.path.join(in_path,im)
    outp=os.path.join(out_path,im)
    ra=black_pixel_ratio(im_path)
    im = cv2.imread(im_path)
    print(im_path)
    if ra>0.99:
        continue
    if ra<0.1:
        cv2.imwrite(outp, 255 - im)
    else:
        cv2.imwrite(outp, im)


##多线程

# from PIL import Image
# import cv2
# import os
# from concurrent.futures import ThreadPoolExecutor
#
#
# def black_pixel_ratio(image_path, threshold=30):
#     """
#     计算给定灰度图像中黑色像素的比例。
#     ...
#     """
#     with Image.open(image_path).convert('L') as img:
#         width, height = img.size
#         black_count = 0
#
#         for y in range(height):
#             for x in range(width):
#                 pixel_value = img.getpixel((x, y))
#                 if pixel_value < threshold:
#                     black_count += 1
#
#         total_pixels = width * height
#         ratio = black_count / total_pixels if total_pixels > 0 else 0
#
#     return ratio
#
#
# def process_image(in_path, out_path, image_name):
#     im_path = os.path.join(in_path, image_name)
#     outp = os.path.join(out_path, image_name)
#
#     ra = black_pixel_ratio(im_path)
#     im = cv2.imread(im_path)
#
#     if ra > 0.99:
#         # Skip this image
#         pass
#     elif ra < 0.1:
#         # Invert the image
#         cv2.imwrite(outp, 255 - im)
#     else:
#         # Keep the original image
#         cv2.imwrite(outp, im)
#
#
# in_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
# out_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images_redeal'
#
# os.makedirs(out_path, exist_ok=True)
#
# # 使用 ThreadPoolExecutor 来并发处理图像
# with ThreadPoolExecutor(max_workers=32) as executor:  # 可以根据实际情况调整 max_workers
#     for image in os.listdir(in_path):
#         executor.submit(process_image, in_path, out_path, image)


# from PIL import Image
# import cv2
# import os
# from concurrent.futures import ThreadPoolExecutor
#
# def black_pixel_ratio(image_path, threshold=30):
#     with Image.open(image_path).convert('L') as img:
#         width, height = img.size
#         black_count = sum(1 for y in range(height) for x in range(width) if img.getpixel((x, y)) < threshold)
#         total_pixels = width * height
#         ratio = black_count / total_pixels if total_pixels > 0 else 0
#     return ratio
#
# def process_image(im, in_path, out_path):
#     im_path = os.path.join(in_path, im)
#     outp = os.path.join(out_path, im)
#     ra = black_pixel_ratio(im_path)
#     im = cv2.imread(im_path)
#     if ra > 0.99:
#         return
#     if ra < 0.1:
#         cv2.imwrite(outp, 255 - im)
#     else:
#         cv2.imwrite(outp, im)
#
# in_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images'
# out_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\local_dan+duoheal\all_images_redeal'
#
# os.makedirs(out_path, exist_ok=True)
#
# images = os.listdir(in_path)
#
# # Number of threads in the pool
# num_threads = 4  # You can adjust this number based on your system's capabilities
#
# with ThreadPoolExecutor(max_workers=num_threads) as executor:
#     # Submit tasks to the executor for processing
#     futures = [executor.submit(process_image, im, in_path, out_path) for im in images]
#
#     # Wait for all futures to complete
#     for future in futures:
#         future.result()


