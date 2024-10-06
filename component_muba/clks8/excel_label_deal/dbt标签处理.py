import os.path
import cv2
import pandas as pd

# # 读取CSV文件
df = pd.read_excel(r'D:\sjwlab\meixuewen\all_data\our_data\dbt\org\val\excel.xlsx')
outpath=r'D:\sjwlab\meixuewen\all_data\our_data\dbt\org\val\labels'
os.makedirs(outpath,exist_ok=True)

for index, row in df.iterrows():
    name = row['PatientID']
    Class=row['Class']
    if Class=='benign':
        a=0
    elif Class=='cancer':
        a=1
    filename=os.path.join(outpath,name+'.txt')
    with open(filename, 'w') as file:
        file.write(str(a))