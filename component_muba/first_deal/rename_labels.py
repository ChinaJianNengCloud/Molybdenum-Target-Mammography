import os
import glob

# 设置文件夹路径
folder_path = 'D:\BaiduNetdiskDownload\mass_labels'  # 替换为您的文件夹路径

# 获取所有.txt文件的列表
txt_files = glob.glob(os.path.join(folder_path, '*.txt'))

# 遍历文件列表并重命名
for file in txt_files:
    # 构建新的文件名
    new_file_name = file[:-4] + '-label.txt'
    # 重命名文件
    os.rename(file, new_file_name)

print("所有.txt文件已重命名。")
