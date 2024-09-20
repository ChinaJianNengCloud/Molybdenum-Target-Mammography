##追加形式

import os
import cv2
import pandas as pd
import numpy as np

def dilate_image(img, kernel_size=(7, 7), iterations=7):
    kernel = np.ones(kernel_size, np.uint8)
    dilated_img = cv2.dilate(img, kernel, iterations=iterations)
    return dilated_img

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
#
# filename = 'example.txt'
#
# a, b, c, d = 1, 2, 3, 4
# with open(filename, 'a') as file:
#     file.write(' {} {} {} {}'.format(a, b, c, d))
#
# print("数据已成功追加到文件。")


excel_path=r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\org_mini\archive\MINI-DDSM-Complete-JPEG-8\DataWMask.xlsx'
maskfile_path=r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\org_mini\archive\MINI-DDSM-Complete-PNG-16'
labelsfile_path=r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\one\resize_redeal\org\test_labels'

os.makedirs(labelsfile_path,exist_ok=True)
df = pd.read_excel(excel_path)
# 遍历DataFrame，打印每一行的X和Y值

for index, row in df.iterrows():
    labelname = row['fileName'][:-4]+'_label.txt'
    maskpath_de=row['Tumour_Contour']
    if maskpath_de=='-':
        continue
    print(labelname,maskpath_de)
    # break
    label_path=os.path.join(labelsfile_path,labelname)
    # with open(label_path, 'a') as file:
    #     file.write(' {} {} {} {}'.format(a, b, c, d))
    mask_path=os.path.join(maskfile_path,maskpath_de)
    mask_path=mask_path[:-4]+'.png'
    print(mask_path)
    mask=cv2.imread(mask_path)
    if mask is None:
        raise ValueError("Image not found or unable to be read.")
    img_dilated = dilate_image(mask)
    img_with_min_rect, box = find_and_draw_bounding_box(img_dilated, mask)

    # print(img_with_min_rect.shape)
    # print(box, mask.shape[:-1])
    # break
    h,w=mask.shape[:-1]
    # print(w,h)
    a=(box[0]+(box[2]/2))/w
    b=(box[1]+(box[3]/2))/h
    c=box[2]/w
    d=box[3]/h
    with open(label_path, 'a') as file:
        file.write(' {} {} {} {}'.format(a, b, c, d))



