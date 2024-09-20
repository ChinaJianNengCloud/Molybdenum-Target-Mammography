import os.path
import cv2
import pandas as pd

df = pd.read_excel(r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\one\all_images\DBT.xlsx')
outpath=r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\one\all_images\locate_labels2'
os.makedirs(outpath,exist_ok=True)

image_path=r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\one\all_images\images'
for index, row in df.iterrows():
    name = row['PatientID_VolumeSlices_Slice']
    impath=os.path.join(image_path,name+'.png')
    im=cv2.imread(impath,0)
    height, width = im.shape
    Width=float(row['Width'])
    Height=float(row['Height'])
    W=Width/width
    H=Height/height
    x = (float(row['X'])+Width/2)/width
    y = (float(row['Y'])+Height/2)/height
    Class=row['Class']
    if Class=='benign':
        flag=0
    elif Class=='cancer':
        flag=1
    with open(os.path.join(outpath,name+'.txt'), 'w') as file:
        file.write(f"{flag} {x} {y} {W} {H}\n")


# image_path=r'D:\sjwlab\meixuewen\all_data\our_data\dbt\afterdeal_dbt\one\all_images\images'
# for index, row in df.iterrows():
#     name = row['PatientID_VolumeSlices_Slice']
#     impath=os.path.join(image_path,name+'.png')
#     im=cv2.imread(impath,0)
#     height, width = im.shape
#     print(name,height,width)
#     break