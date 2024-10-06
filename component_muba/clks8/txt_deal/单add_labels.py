import os
from concurrent.futures import ThreadPoolExecutor

image_path = r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\one\all_images\2(health)'
txt_path = r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\one\all_images\he_labels'

if not os.path.exists(txt_path):
    os.makedirs(txt_path)

def create_txt_file(filename):
    file_base, file_extension = os.path.splitext(filename)
    txt_file_path = os.path.join(txt_path, file_base + '_label.txt')

    with open(txt_file_path, 'w') as file:
        file.write('2')

with ThreadPoolExecutor() as executor:
    for filename in os.listdir(image_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            executor.submit(create_txt_file, filename)

print("所有txt文件创建完毕。")