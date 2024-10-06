# import os
# import cv2
#
# image_path = r'D:\wuwei\Meixw\cbis_chi_duo_Benign'
# ouput_path=r'D:\wuwei\Meixw\cbis_chi_duo_Benign_reser'
#
# for filename in os.listdir(image_path):
#     if filename.endswith('.jpg') or filename.endswith('.png'):
#         im=cv2.imread(os.path.join(image_path,filename))
#         imflip=cv2.flip(im, 1)
#         print(os.path.join(ouput_path,'flip_'+filename))
#         cv2.imwrite(os.path.join(ouput_path,'flip_'+filename),imflip)


###多线程化
import os
import cv2
from concurrent.futures import ThreadPoolExecutor

image_path = r'D:\wuwei\Meixw\first_data\cbis_chi_duo_Cancer'
output_path = r'D:\wuwei\Meixw\second_data\cbis_chi_duo_Cancer_cflip'

if not os.path.exists(output_path):
    os.makedirs(output_path)


def flip_and_save_image(filename):
    input_image_path = os.path.join(image_path, filename)
    output_image_path = os.path.join(output_path, 'cflip' + filename)

    im = cv2.imread(input_image_path)
    if im is None:
        print(f"Error reading image {input_image_path}")
        return
    imflip = cv2.flip(im, 1)
    cv2.imwrite(output_image_path, imflip)
    print(f"Flipped image saved to {output_image_path}")

# 使用ThreadPoolExecutor来创建多线程
with ThreadPoolExecutor() as executor:
    for filename in os.listdir(image_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            executor.submit(flip_and_save_image, filename)
print("所有图片翻转完毕。")

