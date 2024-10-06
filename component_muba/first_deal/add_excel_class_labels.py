import os
import pandas as pd

# 读取Excel文件
df = pd.read_excel('D:\pythonwork\pythonProject\DDSMchange\\note\\note.xlsx')
public_path='D:\pythonwork\pythonProject\DDSMchange\labels'
weiba_dir = '.txt'
for index, row in df.iterrows():
    # 提取A列的图片路径
    mid_patha = row['fileName']
    mid_pathb = row['Side']
    mid_pathc = row['View']
    flag=row['Status']
    f=9
    txtpath=os.path.join(public_path,'folder_'+mid_patha+'.'+mid_pathb+'_'+mid_pathc+weiba_dir)
    if flag=='Benign':
        f=0
    elif flag=='Cancer':
        f=1
    with open(txtpath, 'r') as file:
        original_data = file.read()

    # 打开文件，写入新数据，然后追加原始内容
    with open(txtpath, 'w') as file:
        file.write(str(f))
        file.write(original_data)


