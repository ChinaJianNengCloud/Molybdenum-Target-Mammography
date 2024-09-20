import cv2
import numpy as np
import os

def zuidabaiselt(img):
    image[:30, :] = 0  # 上边30个像素
    image[-30:, :] = 0  # 下边30个像素
    image[:, :30] = 0  # 左边30个像素
    image[:, -30:] = 0  # 右边30个像素
    target_height = 512
    target_width = 256
    gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # top_cut = 40
    # bottom_cut = 40
    # left_cut = 40
    # right_cut = 40
    # gray_image = gray_image1[top_cut:-bottom_cut, left_cut:-right_cut]
    # gray_image=gray_image1
    _, binary_image = cv2.threshold(gray_image1, 8, 255, cv2.THRESH_BINARY)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image)

    largest_area_index = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1

    result_image = np.zeros_like(gray_image1)

    # 将非最大连通区域在钼靶图像上对应位置的区域全部涂黑
    result_image[labels == largest_area_index] = gray_image1[labels == largest_area_index]
    rgb_image = cv2.cvtColor(result_image, cv2.COLOR_GRAY2BGR)
    return  rgb_image


# image = cv2.imread(r'D:\sjwlab\meixuewen\all_data\our_data\mias\afterdeal_mias\redealall\images_cro\mdb012.tif'
#                    )
# image[:30, :] = 0       # 上边30个像素
# image[-30:, :] = 0      # 下边30个像素
# image[:, :30] = 0       # 左边30个像素
# image[:, -30:] = 0      # 右边30个像素
# # 读取灰度图像
# target_height = 512
# target_width = 256
# gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # top_cut = 40
# # bottom_cut = 40
# # left_cut = 40
# # right_cut = 40
# # gray_image = gray_image1[top_cut:-bottom_cut, left_cut:-right_cut]
# # gray_image=gray_image1
# # 将灰度图像转换为二值图像
# _, binary_image = cv2.threshold(gray_image1, 8, 255, cv2.THRESH_BINARY)
#
# # 查找连通区域
# num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image)
#
# # 找到面积最大的连通区域（排除背景）
# largest_area_index = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
#
# # 创建一个与灰度图像尺寸相同的图像，初始化为全黑
# result_image = np.zeros_like(gray_image1)
#
# # 将非最大连通区域在钼靶图像上对应位置的区域全部涂黑
# result_image[labels == largest_area_index] = gray_image1[labels == largest_area_index]
# rgb_image = cv2.cvtColor(result_image, cv2.COLOR_GRAY2BGR)
# cv2.imwrite('output.png',rgb_image)


imfile=r'D:\sjwlab\meixuewen\all_data\our_data\mias\afterdeal_mias\redealall\mask_org'
outfile=r'D:\sjwlab\meixuewen\all_data\our_data\mias\afterdeal_mias\redealall\mask_redeal'
os.makedirs(outfile,exist_ok=True)
for im in os.listdir(imfile):
    impath=os.path.join(imfile,im)
    image=cv2.imread(impath)
    rmask=zuidabaiselt(image)
    cv2.imwrite(os.path.join(outfile,im),rmask)