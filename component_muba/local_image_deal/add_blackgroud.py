# import cv2
# import os
# input_path=r'D:\wuwei\Meixw\first_data\cbis_chi_duo_Cancer\1.3.6.1.4.1.9590.100.1.2.103693117011355566031187716353408415086-1-129.png'
# outpath=r'D:\wuwei\Meixw\midsuing'
# image = cv2.imread(input_path, cv2.IMREAD_COLOR)
#
# if image is not None:
#
#     channels = cv2.split(image)
#     equalized_channels = [cv2.equalizeHist(ch) for ch in channels]
#     equalized_image = cv2.merge(equalized_channels)
#
#     new_width = 800
#     new_height = 600
#     resized_image1 = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
#     resized_image2 = cv2.resize(equalized_image, (new_width, new_height), interpolation=cv2.INTER_AREA)
#     # cv2.imwrite(os.path.join(outpath,'equcsaw2png.png'),equalized_image)
#     cv2.imwrite(os.path.join(outpath, 'equcbis4jpg.jpg'),equalized_image)
#     cv2.imshow('orim',resized_image1)
#     cv2.imshow('im',resized_image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# def enhance_contrast(image, alpha, beta):
#
#   enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
#
#   return enhanced_image
#
#
# input_image = cv2.imread(r'D:\wuwei\Meixw\fimages\processed_images_train\1.3.6.1.4.1.9590.100.1.2.106832350711479350922653707992020709218-1-199.jpg')
#
# alpha = 1.5
# beta = 0
#
#
# enhanced_image = enhance_contrast(input_image, alpha, beta)
# new_width = 800
# new_height = 600
# resized_image1 = cv2.resize(input_image, (new_width, new_height), interpolation=cv2.INTER_AREA)
# resized_image2 = cv2.resize(enhanced_image, (new_width, new_height), interpolation=cv2.INTER_AREA)
# cv2.imshow('orim',resized_image1)
# cv2.imshow('im',resized_image2)


# import cv2
# im=cv2.imread(r'D:\wuwei\Meixw\first_data\cbis_chi_duo_Benign\1.3.6.1.4.1.9590.100.1.2.100131208110604806117271735422083351547-1-126.png')
# flipped_image_vertical = cv2.flip(im, 0)
# new_width = 800
# new_height = 600
# resized_image1 = cv2.resize(flipped_image_vertical, (new_width, new_height), interpolation=cv2.INTER_AREA)
# cv2.imshow('im',resized_image1)


#
# 读取图像
# image = cv2.imread(r'D:\wuwei\Meixw\midsuing\result1.jpg', cv2.IMREAD_GRAYSCALE)
# _, binary1 = cv2.threshold(image, 14, 255, cv2.THRESH_BINARY)
# binary = cv2.bitwise_not(binary1)
# contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# new_width = 800
# new_height = 600
# resized_image2 = cv2.resize(binary, (new_width, new_height), interpolation=cv2.INTER_AREA)
# cv2.imshow('org', resized_image2)
# resized_image3 = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
# cv2.imshow('org1', resized_image3)
# # 假设我们找到至少一个轮廓
# if len(contours) > 0:
#     max_contour = max(contours, key=cv2.contourArea)
#     cv2.drawContours(image, [max_contour], -1, (255, 255, 255), 3)
#     black_image = np.zeros(binary.shape, dtype=np.uint8)
#     cv2.drawContours(black_image, [max_contour], -1, (255, 255, 255), -1)
#
#     new_width = 800
#     new_height = 600
#     resized_image1 = cv2.resize(black_image, (new_width, new_height), interpolation=cv2.INTER_AREA)
#     cv2.imshow('im',resized_image1)
#     cv2.imwrite(r'D:\wuwei\Meixw\midsuing\result4.jpg',black_image)
#     # resized_image2 = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
#     # cv2.imshow('org', resized_image2)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# else:
#     print("No contours found")
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import os
import numpy as np
# # 读取原图和mask
# original_image = cv2.imread(r'D:\wuwei\Meixw\second_data\mini\mini-healhy\mddsm-21.jpg')
# mask = cv2.imread(r'D:\wuwei\Meixw\second_data\mini_mask\mini-healhy\mddsm-21\0.png', 0)  # 0表示加载为灰度图像
def quza(original_image,mask):
    mask = cv2.resize(mask, (original_image.shape[1], original_image.shape[0]), interpolation=cv2.INTER_NEAREST)
    # 确保mask是二值图像（黑和白），这里设置黑色为未选择区域！！！！！！！！！！！！！！
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY_INV)
    # height, width, channels = original_image.shape
    # print(original_image.shape)
    # print(mask.shape)
    # mask = cv2.resize(mask, (height, width), interpolation=cv2.INTER_AREA)
    # 将mask中的白色部分对应的原图区域保留，黑色部分对应的原图区域转换为黑色！！！！！！！！！！！
    result_image = cv2.bitwise_or(original_image, original_image, mask=mask)
    return result_image
def remove_file_extension(filename):
    # 使用os.path.splitext来分割文件名和拓展名！！！！
    base_name = os.path.splitext(filename)[0]
    return base_name
# cv2.imwrite('path_to_result_image.jpg', result_image)
# cv2.imshow('Result', result_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
input_folder = r'D:\wuwei\Meixw\second_data\minideal2\sub'
output_folder = r'D:\wuwei\Meixw\second_data\minideal2\f_images'
pumaskpath= r'D:\wuwei\Meixw\second_data\minideal2\de_masks'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        image = cv2.imread(input_path, cv2.IMREAD_COLOR)
        maskpath1=os.path.join(pumaskpath,
                               # remove_file_extension(filename)
                               filename
                               )
        # for maskname2 in os.listdir(maskpath1):
        #     if maskname2.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                # maskpath3=os.path.join(maskpath1,maskname2)
        maskk=cv2.imread(maskpath1,0)
        result=quza(image,maskk)
        cv2.imwrite(output_path,result)



