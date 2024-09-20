###加快运行
import shutil
import os
import cv2
from concurrent.futures import ThreadPoolExecutor

org_path = r'M:\sjwlab\meixuewen\onelocalimages_view'
outsave_path = r'M:\sjwlab\meixuewen\onelocalimages_bigsizesave'
os.makedirs(outsave_path, exist_ok=True)


def calculate_average_width(directory):
    sum_width = 0
    count = 0
    for imfile in os.listdir(directory):
        impath = os.path.join(directory, imfile)
        img = cv2.imread(impath)
        sum_width += img.shape[1]
        count += 1
    average = sum_width / count if count > 0 else 0
    return average + 1500  # 提高阈值


def process_image(impath, imoutpath, threshold):
    img = cv2.imread(impath)
    if img.shape[1] > threshold:
        shutil.move(impath, imoutpath)


def process_directory(directory, outdirectory, threshold):
    with ThreadPoolExecutor(max_workers=48) as executor:
        for imfile in os.listdir(directory):
            impath = os.path.join(directory, imfile)
            imoutpath = os.path.join(outdirectory, imfile)
            executor.submit(process_image, impath, imoutpath, threshold)


for idfile in os.listdir(org_path):
    idpath = os.path.join(org_path, idfile)
    idoutpath = os.path.join(outsave_path, idfile)
    os.makedirs(idoutpath, exist_ok=True)

    for viewfile in os.listdir(idpath):
        viewpath = os.path.join(idpath, viewfile)
        viewoutpath = os.path.join(idoutpath, viewfile)
        os.makedirs(viewoutpath, exist_ok=True)

        average = calculate_average_width(viewpath)
        process_directory(viewpath, viewoutpath, average)