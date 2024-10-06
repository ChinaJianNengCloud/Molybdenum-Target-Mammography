import cv2
import numpy as np


def dilate_image(img, kernel_size=(7, 7), iterations=7):
    kernel = np.ones(kernel_size, np.uint8)
    dilated_img = cv2.dilate(img, kernel, iterations=iterations)
    return dilated_img


def find_and_draw_largest_contour_with_min_rect(img, imgorg):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        raise ValueError("No contours found.")

    largest_contour = max(contours, key=cv2.contourArea)
    rect = cv2.minAreaRect(largest_contour)
    box = cv2.boxPoints(rect)
    # box = np.int0(box)
    box = box.astype(np.int32)
    # 在原图上绘制最小外接矩形（非实心）
    cv2.drawContours(imgorg, [box], 0, (0, 255, 0), 2)

    # # 根据最小外接矩形的坐标裁剪图像
    # x_min, y_min = np.min(box, axis=0)
    # x_max, y_max = np.max(box, axis=0)
    # cropped_img = imgorg[y_min:y_max, x_min:x_max]

    return imgorg ,box


def find_and_draw_bounding_box(img, imgorg):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        raise ValueError("No contours found.")

    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    box=x, y, w, h
    # 在原图上绘制直立的边界框
    cv2.rectangle(imgorg, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return imgorg,box
def resize_image(img, output_size=(600, 800)):

    if img is None:
        raise ValueError("无法读取图像或路径不正确")

    width, height = output_size
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    return resized_img

def crop_image_edges(img, crop_size=3):
    if len(img.shape) != 3 or img.shape[2] != 3:
        raise ValueError("Input image is not a three-channel image.")

    cropped_img = img[crop_size:-crop_size, crop_size:-crop_size]
    return cropped_img


input_path = r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\org_mini\archive\MINI-DDSM-Complete-JPEG-8\Benign\0029\C_0029_1.LEFT_CC_Mask.jpg'

img = cv2.imread(input_path)
if img is None:
    raise ValueError("Image not found or unable to be read.")

# 先裁剪边缘，再膨胀，最后找到最大轮廓并裁剪
# img_cropped = crop_image_edges(img)
img_cropped = img
img_dilated = dilate_image(img_cropped)
img_with_min_rect,box = find_and_draw_bounding_box(img_dilated, img_cropped)

print(img_with_min_rect.shape)
print(box,img.shape[:-1])
cv2.imshow('equtest.png', resize_image(img_with_min_rect))

cv2.waitKey(0)
cv2.destroyAllWindows()