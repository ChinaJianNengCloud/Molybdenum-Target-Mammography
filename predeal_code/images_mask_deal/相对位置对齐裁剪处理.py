import cv2
import numpy as np
import os
from concurrent.futures import ThreadPoolExecutor
import threading



def crop_image_from_right(img, crop_width):
    height, width = img.shape[:2]
    if crop_width <= 0 or crop_width > width:
        raise ValueError("裁剪宽度不合理，请选择一个合适的宽度")
    return img[:, 0:width - crop_width]

def crop_image_from_bottom(img, crop_height):
    height, width = img.shape[:2]
    if crop_height <= 0 or crop_height > height:
        raise ValueError("裁剪高度不合理，请选择一个合适的高度")
    return img[0:height - crop_height, :]

def crop_image(image, top, left):
    if image is None:
        print("Error: 图像无法加载！")
        return None
    height, width = image.shape[:2]
    new_top = top
    new_left = left
    new_height = height - top
    new_width = width - left
    return image[new_top:new_top + new_height, new_left:new_left + new_width]

def right_black(image):
    if image is None:
        print("Error: 图像无法加载！")
        exit(-1)
    black_pixel_col = -1
    for x in range(image.shape[1] - 1, -1, -1):
        col = image[:, x]
        black_pixels_count = np.sum(col == 0)
        ratio_black_pixels = black_pixels_count / col.size
        if ratio_black_pixels < 0.9:
            black_pixel_col = x
            break
    return image.shape[1] - black_pixel_col - 1

def bottom_black(image):
    if image is None:
        print("Error: 图像无法加载！")
        exit(-1)
    black_pixel_row = -1
    for y in range(image.shape[0] - 1, -1, -1):
        row = image[y, :]
        black_pixels_count = np.sum(row == 0)
        ratio_black_pixels = black_pixels_count / row.size
        if ratio_black_pixels < 0.9:
            black_pixel_row = y
            break
    return image.shape[0] - black_pixel_row - 1

def topleftget(image):
    if image is None:
        print("Error: 图像无法加载！")
        exit(-1)
    black_pixel_row = -1
    black_pixel_column = -1
    for y in range(image.shape[0]):
        row = image[y, :]
        black_pixels_count = np.sum(row == 0)
        ratio_black_pixels = black_pixels_count / row.size
        if ratio_black_pixels < 0.98:
            black_pixel_row = y
            break
    for x in range(image.shape[1]):
        column = image[:, x]
        black_pixels_count = np.sum(column == 0)
        ratio_black_pixels = black_pixels_count / column.size
        if ratio_black_pixels < 0.96:
            black_pixel_column = x
            break
    return black_pixel_row, black_pixel_column

# 输入和输出路径
imgfile = r'M:\sjwlab\meixuewen\onelocalimages_view'
outpath = r'M:\sjwlab\meixuewen\onelocalimages_view_cro'
os.makedirs(outpath, exist_ok=True)

# 创建一个线程锁
lock = threading.Lock()

# 定义处理函数
def process_image(impath):
    try:
        img = cv2.imread(impath, 0)

        right = right_black(img)
        if right != 0:
            img = crop_image_from_right(img, right)

        bottom = bottom_black(img)
        if bottom != 0:
            img = crop_image_from_bottom(img, bottom)

        top, left = topleftget(img)
        if top != -1 and left != -1:
            img = crop_image(img, top, left)

        with lock:  # 使用锁来同步对输出文件的写入
            out_folder = os.path.dirname(impath).replace(imgfile, outpath)
            os.makedirs(out_folder, exist_ok=True)
            output_path = os.path.join(out_folder, os.path.basename(impath))
            cv2.imwrite(output_path, img)
    except Exception as e:
        print(f"Error processing {impath}: {e}")

# 创建一个线程池
with ThreadPoolExecutor(max_workers=48) as executor:  # 可以根据实际情况调整 max_workers 的大小
    # 遍历文件夹
    for idfile in os.listdir(imgfile):
        idfilepath = os.path.join(imgfile, idfile)
        for viewfile in os.listdir(idfilepath):
            viewpath = os.path.join(idfilepath, viewfile)
            for im in os.listdir(viewpath):
                impath = os.path.join(viewpath, im)
                executor.submit(process_image, impath)

print("所有任务已完成。")