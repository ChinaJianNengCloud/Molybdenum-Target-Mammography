import cv2
import numpy as np
import os
from txtmath import mymath
# 读取图像
outpath='D:\pythonwork\pythonProject\DDSMchange\labels'
weiba_dir = '.txt'
def mydrawnote(path1,path2,txtname):
   outpathtxt = os.path.join(outpath,txtname+weiba_dir)
   im = cv2.imread(path1)
   image=cv2.imread(path2)
   im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

   t, bin = cv2.threshold(im_gray, 127,
                       255,
                       cv2.THRESH_BINARY)
   cnts, hie = cv2.findContours(bin,
                             cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_NONE)

   mask = np.zeros(bin.shape, np.uint8)
   im_fill = cv2.drawContours(mask, cnts,  # 填充
                           -1, (255, 0, 0), -1)

   im_sub = cv2.subtract(im_fill, bin)

   k = np.ones((3, 3), np.uint8)

   im_close = cv2.morphologyEx(im_sub, cv2.MORPH_CLOSE, k, iterations=2)
   cnts, hie = cv2.findContours(im_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   contour=cnts[0]
   x, y, w, h = cv2.boundingRect(contour)
   a,b,c,d=mymath(x, y, w, h)
   with open(outpathtxt, 'w', encoding='utf-8') as file:
       file.write(f"  {a}  {b}  {c}  {d}\n")
   cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
   return image
'''
im_cnt = cv2.drawContours(im,
                          cnts,
                          -1,
                          (0, 0, 255),
                          2)
'''
  # output_path = 'D:\pythonwork\pythonProject\DDSMchange\\notedrawtest\output_image.jpg'
  # cv2.imwrite(outpath, image)

