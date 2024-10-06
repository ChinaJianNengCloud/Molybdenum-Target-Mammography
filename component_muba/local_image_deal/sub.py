import cv2
import numpy as np
import os


# image1 = cv2.imread('D:\wuwei\Meixw\midsuing\cbisorg.png')
# image2 = cv2.imread(r'D:\wuwei\Meixw\midsuing\ccount2.jpg')
#
# # print(image1.shape)
# # print(image2.shape)
# # 确保两幅图像具有相同的大小!!!
# if image1.shape != image2.shape:
#     image2 = cv2.resize(image2, image1.shape[:2][::-1])
#
# im = image2-33
# print(im
# )
#
#
#
# # image = cv2.imread('D:\wuwei\Meixw\midsuing\ccount2.jpg', cv2.IMREAD_GRAYSCALE)
# #
# # # 应用中值滤波
# # # ksize是中值滤波器的核大小，它必须是奇数
# # filtered_image = cv2.medianBlur(image, ksize=5)
#
#
#
# new_width = 800
# new_height = 600
#
# resized_image1 = cv2.resize(im ,(new_width, new_height), interpolation=cv2.INTER_AREA)
# # cv2.imwrite(r'D:\wuwei\Meixw\midsuing\result1.jpg',im)
# cv2.imshow('Fused Image', resized_image1)
#
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


input_folder = r'D:\wuwei\Meixw\second_data\minideal2\de_images'
output_folder = r'D:\wuwei\Meixw\second_data\minideal2\sub'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        image = cv2.imread(input_path, cv2.IMREAD_COLOR)

        if image is not None:

            # channels = cv2.split(image)
            # equalized_channels = [cv2.equalizeHist(ch) for ch in channels]
            # equalized_image = cv2.merge(equalized_channels)
            subed_image=image-31
            cv2.imwrite(output_path, subed_image)

print("sub完成，处理后的图片已保存到:", output_folder)
