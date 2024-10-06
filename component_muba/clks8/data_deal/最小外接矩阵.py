import cv2
import numpy as np
def resize_image(img, output_size=(600, 800)):

    if img is None:
        raise ValueError("无法读取图像或路径不正确")

    width, height = output_size
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    return resized_img
a,b,c,d=0.32534843205574915, 0.45666423889293517, 0.19773519163763068, 0.08011653313911143




# w,h=2826,6601
image_path = r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\one\resize_redeal\org\mini\all_images_dtext\A_1576_1.RIGHT_MLO.png'
image = cv2.imread(image_path,0)

h,w=image.shape

# print(h,w)
a=a*w
b=b*h
c=c*w
d=d*h

# 计算矩形的左上角和右下角坐标
left_top = (int(a - c / 2), int(b - d / 2))
right_bottom = (int(a + c / 2), int(b + d / 2))
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.rectangle(image, left_top, right_bottom, (255, 255, 0), 3)

cv2.imshow('Rectangle', resize_image(image))
cv2.waitKey(0)
cv2.destroyAllWindows()