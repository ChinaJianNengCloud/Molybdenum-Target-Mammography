import os


def check_file_exists(filename):
    """
    检查给定的文件是否存在。

    参数:
    filename (str): 要检查的文件的完整路径。

    返回:
    bool: 如果文件存在返回 True，否则返回 False。
    """
    return os.path.exists(filename)


# print(check_file_exists(r"D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\two\meixw\labels\DBT-P00001.txt"))

image_path=r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\two\meixw\meixwdeal'
txt_path=r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\two\meixw\labels'
for im in os.listdir(image_path):
    tpath=os.path.join(txt_path,im+'.txt')
    if check_file_exists(tpath)==False:
        with open(tpath, 'w') as file:
            file.write(str(2))

