import cv2
import numpy as np
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from threading import Lock


def check_image_symmetry(image):
    # 将图像转换为灰度图
    gray = image

    # 计算图像的水平翻转
    flipped = cv2.flip(gray, 1)

    # 计算原始图像和翻转图像之间的差异
    diff = cv2.absdiff(gray, flipped)

    # 对差异图像进行二值化处理
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # 计算非零像素的数量，即差异的总和
    non_zero_pixels = np.count_nonzero(thresh)

    # 计算对称性得分（差异像素占总像素的比例）
    symmetry_score = non_zero_pixels / (gray.shape[0] * gray.shape[1])

    return symmetry_score

file_path = r'J:\sjwlab\meixuewen\twolocalimages'
out_path = r'J:\sjwlab\meixuewen\twolocalimages_view'
os.makedirs(out_path, exist_ok=True)

# 定义一个锁对象
lock = Lock()


def process_directory(idpath, out_path):
    out_dir = os.path.join(out_path, os.path.basename(idpath))
    os.makedirs(out_dir, exist_ok=True)

    scores = []
    images = []

    for im in os.listdir(idpath):
        impath = os.path.join(idpath, im)
        image = cv2.imread(impath)
        original_image = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        score = check_image_symmetry(thresh)
        scores.append(score)
        images.append((original_image, im))

    average = np.mean(scores)

    with lock:
        for (original_image, im), score in zip(images, scores):
            if score >= average:
                out1 = os.path.join(out_dir, 'cc')
                os.makedirs(out1, exist_ok=True)
                cv2.imwrite(os.path.join(out1, im), original_image)
            else:
                out2 = os.path.join(out_dir, 'mlo')
                os.makedirs(out2, exist_ok=True)
                cv2.imwrite(os.path.join(out2, im), original_image)


def main():
    with ProcessPoolExecutor(max_workers=48) as executor:
        futures = [executor.submit(process_directory, os.path.join(file_path, idfile), out_path) for idfile in
                   os.listdir(file_path)]
        for future in as_completed(futures):
            future.result()


if __name__ == '__main__':
    main()
