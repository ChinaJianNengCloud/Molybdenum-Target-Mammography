import cv2
import os


def remove_file_extension(filename):
    # 使用os.path.splitext来分割文件名和拓展名
    base_name = os.path.splitext(filename)[0]
    return base_name

def delatexs(image):
    height, width = image.shape[:2]

    cropped_image = image[margin:height - margin, margin:width - margin]
    return cropped_image

margin = 40   #(xiangsu# )


input_folder = r'D:\wuwei\Meixw\second_data\minideal2\equ'
output_folder = r'D:\wuwei\Meixw\second_data\minideal2\de_images'
maskout_path = r'D:\wuwei\Meixw\second_data\minideal2\de_masks'
pumaskpath=r'E:\wuwei\project\1_Singleview_classify\Meixwdeal\segment-anything-main\scripts\final2'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        image = cv2.imread(input_path, cv2.IMREAD_COLOR)
        maskpath1=os.path.join(pumaskpath,remove_file_extension(filename))
        for maskname2 in os.listdir(maskpath1):
            if maskname2.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                maskpath3=os.path.join(maskpath1,maskname2)
                maskk=cv2.imread(maskpath3,0)
        croimages=delatexs(image)
        cv2.imwrite(output_path,croimages)
        cromask=delatexs(maskk)
        cv2.imwrite(os.path.join(maskout_path,filename),cromask)