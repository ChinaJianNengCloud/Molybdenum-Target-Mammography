import os
import shutil

images_path=r'D:\sjwlab\meixuewen\all_data\our_data\DMID\DMID_afterdead\one\DMIDdan_rechoise'
labels_path=r'D:\sjwlab\meixuewen\all_data\our_data\DMID\DMID_afterdead\one\labels'
outputlabels=r'D:\sjwlab\meixuewen\all_data\our_data\DMID\DMID_afterdead\one\relabels'

os.makedirs(outputlabels,exist_ok=True)

for file in os.listdir(images_path):
    txtpath=os.path.join(labels_path,file[:-4]+'.txt')
    out=os.path.join(outputlabels,file[:-4]+'.txt')
    shutil.copyfile(txtpath,out)