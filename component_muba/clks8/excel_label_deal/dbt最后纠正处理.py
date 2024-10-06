import os
import cv2
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# 定义输入输出路径
file_path = Path(r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\two\meixw\images')
out = Path(r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\two\meixw\reimages')

# 创建输出目录
os.makedirs(out, exist_ok=True)


# 并行化处理
def process_directory(idpath: Path, idout: Path):
    os.makedirs(idout, exist_ok=True)
    for imfile in os.listdir(idpath):
        if imfile.endswith('.png'):  # 假设只处理 .png 文件
            impath = idpath / imfile
            img = cv2.imread(str(impath))
            name = imfile[:-8] + '.png'
            cv2.imwrite(str(idout / name), img)


# 使用线程池执行并行任务
with ThreadPoolExecutor(max_workers=16) as executor:
    futures = []
    for idfile in os.listdir(file_path):
        idpath = file_path / idfile
        idout = out / idfile
        future = executor.submit(process_directory, idpath, idout)
        futures.append(future)

    # 等待所有任务完成
    for future in as_completed(futures):
        future.result()

print("所有文件处理完毕")