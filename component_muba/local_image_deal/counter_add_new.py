import cv2
import numpy as np
import os


def remove_file_extension(filename):
    base_name = os.path.splitext(filename)[0]
    return base_name


def addc(image, mask1):
    kernel = np.ones((3, 3), np.uint8)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel, iterations=8)

    height, width, channels = image.shape
    mask = cv2.resize(mask1, (width, height), interpolation=cv2.INTER_AREA)

    # mask_blurred = cv2.GaussianBlur(mask, (5, 5), 0)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        # 对轮廓进行近似，epsilon是一个控制近似精度的参数
        epsilon = 0.0030 * cv2.arcLength(max_contour, True)
        approx_contour = cv2.approxPolyDP(max_contour, epsilon, True)
        # 使用cv2.LINE_AA绘制平滑的线条
        cv2.drawContours(image, [approx_contour], -1, (180, 180, 180), 15, lineType=cv2.LINE_AA)
    return image



input_folder = r'D:\wuwei\Meixw\second_data\minideal2\f_images'
output_folder = r'D:\wuwei\Meixw\second_data\minideal2\f_images2'
pumaskpath=r'D:\wuwei\Meixw\second_data\minideal2\de_masks'


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        image = cv2.imread(input_path, cv2.IMREAD_COLOR)
        maskpath1 = os.path.join(pumaskpath, filename)
        maskk = cv2.imread(maskpath1, 0)
        result = addc(image, maskk)
        cv2.imwrite(output_path, result)
