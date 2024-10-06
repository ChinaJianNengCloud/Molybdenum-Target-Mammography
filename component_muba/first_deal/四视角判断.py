import os

import cv2


def f_mlo(path):
    # 读取图像
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # 裁剪图像：去除左右上下各5像素
    # cropped_image = image[5:-5, 5:-5]
    cropped_image = image
    # 获取裁剪后图像的高度和宽度
    height, width = cropped_image.shape[:2]
    left_half = cropped_image[:, :width // 2]
    right_half = cropped_image[:, width // 2:]
    left_sum = cv2.sumElems(left_half)[0]
    right_sum = cv2.sumElems(right_half)[0]
    left_true = (left_sum > right_sum)
    # 分别获取图像的上、下、左、右边界像素
    top_pixels = cropped_image[0, :]
    bottom_pixels = cropped_image[height - 1, :]
    left_pixels = cropped_image[:, 0]
    right_pixels = cropped_image[:, width - 1]

    # 统计非黑像素数量
    top_nonzero = cv2.countNonZero(top_pixels)
    bottom_nonzero = cv2.countNonZero(bottom_pixels)
    left_nonzero = cv2.countNonZero(left_pixels)
    right_nonzero = cv2.countNonZero(right_pixels)

    # 计算边界长度
    top_length = width
    bottom_length = width
    left_length = height
    right_length = height

    # 检查非黑像素数量是否超过边界长度的 1/8
    threshold = 1 / 8

    count = 0

    if top_nonzero > top_length * threshold:
        count += 1

    if bottom_nonzero > bottom_length * threshold:
        count += 1

    if left_nonzero > left_length * threshold:
        count += 1

    if right_nonzero > right_length * threshold:
        count += 1

    # 如果有两个以上的计数器超过 1，输出图片名
    if count >= 2 and left_true:
        return "lmlo"
    elif count >= 2 and not left_true:
        return "rmlo"
    elif count < 2 and left_true:
        return "lcc"
    elif count < 2 and not left_true:
        return "rcc"

from PIL import Image

def crop_and_save(image_path=0, output_path=0, crop_size=0):

    # 打开图像
    img = Image.open(image_path)

    # 获取图像的宽度和高度
    width, height = img.size

    # 计算上下裁剪的范围
    if "l" == f_mlo(image_path)[0]:
        w=width-120
    # bottom_crop = height - crop_size

    # 裁剪图像
        cropped_img = img.crop((0, 0, width-120, height))
    else:
        cropped_img = img.crop((120, 0, width, height))

    # 保存裁剪后的图像

    cropped_img.save(output_path)
    # cropped_img.show()

# 示例用法
# input_image_path = r"D:\software\WeChat\chat_file\WeChat Files\wxid_sbzzyfx1sa0322\FileStorage\File\2024-01\CR2497601\CR2497601\processed_DXm.1.2.392.200036.9125.4.0.1796158349.53216616.1573523479.png"
output_image_path = r"D:\software\WeChat\chat_file\WeChat Files\wxid_sbzzyfx1sa0322\FileStorage\File\2024-01\1"
# crop_size = 10

# crop_and_save(input_image_path, output_image_path, crop_size)

image_path = r"D:\software\WeChat\chat_file\WeChat Files\wxid_sbzzyfx1sa0322\FileStorage\File\2024-01\CR1525738"
for i in os.listdir(image_path):
    if i.endswith(".png"):
        ima_=os.path.join(image_path,i)
        out_=os.path.join(output_image_path,i)
        crop_and_save(ima_, out_)
