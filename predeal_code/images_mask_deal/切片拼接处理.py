import cv2
import numpy as np
import os

# imagefile_path=r'/data_hs/sjwlab/meixuewen/project2/dataset/localduo_data_redeal/CR2513381LEFT/cc'

def toge(imagefile_path):
    # # 设置分割的数量
    # num_patches = 10
    # 设置分割的数量
    num_patches_height = 20
    num_patches_width = 10
    num_patches = (num_patches_height, num_patches_width)

    for imfile in os.listdir(imagefile_path):
        img_path=os.path.join(imagefile_path,imfile)
        imgbase=cv2.imread(img_path,0)
        height, width = imgbase.shape
            # 计算需要裁剪的尺寸
        crop_height = height % num_patches_height
        crop_width = width % num_patches_width
        if crop_height > 0:
            imgbase= imgbase[:-crop_height, :]
            # im2 = im2[:-crop_height, :]
        if crop_width > 0:
            imgbase = imgbase[:, :-crop_width]
            # im2 = im2[:, :-crop_width]
        # 更新高度和宽度
        height, width = imgbase.shape
        # 初始化新图像
        new_image = np.zeros_like(imgbase)
        break

    for imfile in os.listdir(imagefile_path):
        img_path=os.path.join(imagefile_path,imfile)
        img=cv2.imread(img_path,0)

        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

        # 计算每个patch的大小
        patch_width = width // num_patches[1]  # 使用宽度的分割数
        patch_height = height // num_patches[0]  # 使用高度的分割数

        # 遍历每个小块
        for i in range(num_patches[0]):
            for j in range(num_patches[1]):
                # 提取两个图像的对应小块
                roi1 = imgbase[i*patch_height:(i+1)*patch_height, j*patch_width:(j+1)*patch_width]
                roi2 = img[i*patch_height:(i+1)*patch_height, j*patch_width:(j+1)*patch_width]

                # 计算统计值
                min_val1, max_val1 = roi1.min(), roi1.max()
                avg_val1 = roi1.mean()

                min_val2, max_val2 = roi2.min(), roi2.max()
                avg_val2 = roi2.mean()

                # 根据规则选择保留哪个小块
                value1 = (min_val1 - avg_val1) + (max_val1 - avg_val1)
                value2 = (min_val2 - avg_val2) + (max_val2 - avg_val2)

                if value1 > value2:
                    new_image[i*patch_height:(i+1)*patch_height, j*patch_width:(j+1)*patch_width] = roi1
                else:
                    new_image[i*patch_height:(i+1)*patch_height, j*patch_width:(j+1)*patch_width] = roi2
        imgbase=new_image
    return imgbase

# cv2.imwrite('test_combined_image.png', toge(imagefile_path))


in_path=r'M:\sjwlab\meixuewen\onelocalimages_view_cro'
out_path=r'M:\sjwlab\meixuewen\onelocalimages_view_cro_final'

os.makedirs(out_path,exist_ok=True)
for idfile in os.listdir(in_path):
    idfilepath=os.path.join(in_path,idfile)
    out1_id=os.path.join(out_path,idfile)
    os.makedirs(out1_id,exist_ok=True)
    for viewfile in os.listdir(idfilepath):
        viewpath=os.path.join(idfilepath,viewfile)
        out2_view=os.path.join(out1_id,viewfile+'.png')
        # print(viewpath,out2_view)
        redim=toge(viewpath)
        cv2.imwrite(out2_view,redim)

