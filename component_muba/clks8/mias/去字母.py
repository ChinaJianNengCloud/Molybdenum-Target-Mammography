import os

import cv2

imgpath=r'D:\sjwlab\meixuewen\all_data\our_data\mias\afterdeal_mias\redealall\images'
outpath=r'D:\sjwlab\meixuewen\all_data\our_data\mias\afterdeal_mias\redealall\reimages'

os.makedirs(outpath,exist_ok=True)

for imfile in os.listdir(imgpath):
    imp=os.path.join(imgpath,imfile)
    img=cv2.imread(imp)
    img[img==255]=0
    cv2.imwrite(os.path.join(outpath,imfile),img)