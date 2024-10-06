#修改某列
import os
import glob

folder_path = 'D:\BaiduNetdiskDownload\\rcalc_labels'  # 替换为您的文件夹路径

txt_files = glob.glob(os.path.join(folder_path, '*.txt'))


for file in txt_files:
    with open(file, 'r') as f:
        lines = f.readlines()
    new_lines = [line.split()[0] + '\n' for line in lines]

    with open(file, 'w') as f:
        f.writelines(new_lines)

print("所有.txt文件已修改。")
