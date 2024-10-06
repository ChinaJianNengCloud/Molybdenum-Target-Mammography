import os
import cv2

infile_path=r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\org_mini\archive\MINI-DDSM-Complete-PNG-16\Cancer'
outfile_path=r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\one\redeal\Cancer'

os.makedirs(outfile_path,exist_ok=True)

for file in os.listdir(infile_path):
    imagefilepath=os.path.join(infile_path,file)
    for imagefile in os.listdir(imagefilepath):
        if imagefile.endswith('.png'):
            testimagefile=imagefile[:-4]
            if testimagefile[-2:] == 'CC' or testimagefile[-3:] == 'MLO':
                imagepath=os.path.join(imagefilepath,imagefile)
                img=cv2.imread(imagepath)
                ouputpath=os.path.join(outfile_path,imagefile)
                cv2.imwrite(ouputpath,img)

