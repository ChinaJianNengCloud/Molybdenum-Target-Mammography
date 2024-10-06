import os.path
import cv2
import pandas as pd

# # 读取CSV文件
df = pd.read_excel(r'D:\sjwlab\meixuewen\all_data\our_data\mias\org_mias\all-mias\Info.xlsx')
outpath=r'D:\sjwlab\meixuewen\all_data\our_data\mias\afterdeal_mias\locate_labels2'
os.makedirs(outpath,exist_ok=True)

for index, row in df.iterrows():
    id = row['id']
    severity=row['severity']
    x=row['x']
    y=row['y']
    r=row['r']
    if severity!=None and r>0:
        W=2*r/1024
        H=2*r/1024
        if severity=='B':
            flag=0
        elif severity=='M':
            flag=1
        with open(os.path.join(outpath,id+'_label.txt'), 'w') as file:
            file.write(f"{flag} {x/1024} {y/1024} {W} {H}\n")

    else:
        if severity == 'B':
            flag = 0
        elif severity == 'M':
            flag = 1
        else:
            flag=2
        with open(os.path.join(outpath,id+'_label.txt'), 'w') as file:
            file.write(f"{flag}\n")