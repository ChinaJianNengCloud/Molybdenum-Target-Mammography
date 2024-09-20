# 平均
import cv2
import os
import numpy as np

filepath = r'M:\sjwlab\meixuewen\twolocalimages_view_cro'
fileoutpath = r'M:\sjwlab\meixuewen\zstack\avera'
os.makedirs(fileoutpath, exist_ok=True)


def gjjavera(imagefilepath):
    image_files = os.listdir(imagefilepath)
    image_paths = [os.path.join(imagefilepath, f) for f in image_files]

    sum_image = None
    count = 0
    target_width = None
    target_height = None

    for path in image_paths:
        im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if sum_image is None:
            target_height, target_width = im.shape
            sum_image = np.zeros((target_height, target_width), dtype=np.float32)

        if im.shape[0] != target_height or im.shape[1] != target_width:
            im = cv2.resize(im, (target_width, target_height), interpolation=cv2.INTER_AREA)

        sum_image += im
        count += 1

    average_image = sum_image / count
    average_image = np.uint8(average_image)
    return average_image


for idfile in os.listdir(filepath):
    id_path = os.path.join(filepath, idfile)
    idout_path = os.path.join(fileoutpath, idfile)
    os.makedirs(idout_path, exist_ok=True)
    for viewfile in os.listdir(id_path):
        view_path = os.path.join(id_path, viewfile)
        viewout = os.path.join(idout_path, viewfile + '.png')
        img = gjjavera(view_path)
        cv2.imwrite(viewout, img)

