import cv2
import os

input_folder = r'D:\wuwei\Meixw\second_data\mini\mini-healhy'
output_folder = r'D:\wuwei\Meixw\second_data\minideal2\equ'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        image = cv2.imread(input_path, cv2.IMREAD_COLOR)

        if image is not None:

            channels = cv2.split(image)
            equalized_channels = [cv2.equalizeHist(ch) for ch in channels]
            equalized_image = cv2.merge(equalized_channels)

            cv2.imwrite(output_path, equalized_image)

print("直方图均衡化完成，处理后的图片已保存到:", output_folder)

# def equ(image):
#     if image is not None:
#         channels = cv2.split(image)
#         equalized_channels = [cv2.equalizeHist(ch) for ch in channels]
#         equalized_image = cv2.merge(equalized_channels)
#         return equalized_image
#
# im=cv2.imread('D:\wuwei\Meixw\midsuing\count2.jpg')
# im2=equ(im)
# cv2.imwrite('D:\wuwei\Meixw\midsuing\ccount2.jpg',im2)