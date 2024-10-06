import os

# 设置要遍历的文件夹路径
folder_path = r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\one\all_images\locate_labels2'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否以.txt结尾
    if filename.endswith('.txt'):
        # 构造新的文件名
        new_filename = filename[:-4] + '_label.txt'
        # 构造完整的文件路径
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        # 重命名文件
        os.rename(old_file, new_file)
        print(f'Renamed "{old_file}" to "{new_file}"')
