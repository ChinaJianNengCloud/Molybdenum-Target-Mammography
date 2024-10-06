####通过多线程进行了加速划分，需要注意的是，划分后原文件就没了，如果有必要请备份（meixwadd）
import os
import random
from concurrent.futures import ThreadPoolExecutor


images_folder = r'D:\wuwei\Meixw\images_data'
labels_folder = r'D:\wuwei\Meixw\labels_data'

# 获取图片和标签文件列表
images = [f for f in os.listdir(images_folder) if f.endswith('.jpg') or f.endswith('.png')]
labels = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]

# 创建训练集和测试集的文件夹
train_images_folder = r'D:\wuwei\Meixw\fimages\images_train'
test_images_folder = r'D:\wuwei\Meixw\fimages\images_val'
train_labels_folder = r'D:\wuwei\Meixw\flabels\labels_train'
test_labels_folder = r'D:\wuwei\Meixw\flabels\labels_val'
os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(test_images_folder, exist_ok=True)
os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(test_labels_folder, exist_ok=True)

# 随机划分数据集！
random.seed(0)
train_ratio = 0.7
train_indices = random.sample(range(len(images)), int(len(images) * train_ratio))


def move_file(src, dst):
    os.rename(src, dst)

# 使用线程池执行文件移动操作
with ThreadPoolExecutor() as executor:
    for i, image in enumerate(images):
        label = image[:-4] + '_label.txt'  ###（这里我将标签习惯性设置为该模式，后续可修改）
        if i in train_indices:
            executor.submit(move_file, os.path.join(images_folder, image), os.path.join(train_images_folder, image))
            executor.submit(move_file, os.path.join(labels_folder, label), os.path.join(train_labels_folder, label))
        else:
            executor.submit(move_file, os.path.join(images_folder, image), os.path.join(test_images_folder, image))
            executor.submit(move_file, os.path.join(labels_folder, label), os.path.join(test_labels_folder, label))

print("数据集划分完成。")
