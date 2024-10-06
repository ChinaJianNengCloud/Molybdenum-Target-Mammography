import os
import cv2
from findcounterdraw import mydrawnote
new_folder_path = 'D:\pythonwork\pythonProject\DDSMchange\mydrawnote'
def get_subfolders(root_folder):
    subfolder_names = []  # 创建一个空列表来存储子文件夹名称
    subfolder_paths = []  # 创建一个空列表来存储子文件夹路径
    # 遍历根文件夹下的所有子文件夹
    for item in os.listdir(root_folder):
        # 拼接完整的路径
        full_path = os.path.join(root_folder, item)
        # 判断是否为文件夹
        if os.path.isdir(full_path):
            # 将子文件夹的名称和路径添加到列表中
            subfolder_names.append(item)
            subfolder_paths.append(full_path)
    return subfolder_names, subfolder_paths

# 使用示例
root_folder = 'D:\pythonwork\pythonProject\DDSMchange\\note\\note_images'  # 替换为您的文件夹路径
names, paths = get_subfolders(root_folder)

# 打印返回的子文件夹信息
for name, path in zip(names, paths):
    print(f"子文件夹名称: {name}")
    out_patha=os.path.join(new_folder_path,name)
    os.makedirs(out_patha, exist_ok=True)
    print(f"子文件夹路径: {path}\n")
    for onepp in os.listdir(path):
        if onepp==name[7:]+'.LEFT_CC.jpg':# or onepp==name[7:]+'.RIGHT_CC.jpg':#CCtest
            if not os.path.exists(os.path.join(path, name[7:]+'.LEFT_CC_Mask.jpg')):
                print(f"路径 {paths, name[7:]+'.LEFT_CC_Mask.jpg'} 不存在，跳过")
            else:
                onemaskpath1=os.path.join(path,name[7:]+'.LEFT_CC_Mask.jpg')
                onemaskpath11 = os.path.join(path, name[7:] + '.LEFT_CC.jpg')
                txtname=name+'.LEFT_CC'
                out_path=os.path.join(out_patha,'LEFT_CC.jpg')
                print('onemaskpath1', onemaskpath1)
                print('onemaskpath11', onemaskpath11)
                print('out_path', out_path)
                cv2.imwrite(out_path,mydrawnote(onemaskpath1,onemaskpath11,txtname))#mydrawnote(onemaskpath1,onemaskpath11)

            if not os.path.exists(os.path.join(path, name[7:]+'.LEFT_CC_MASK2.jpg')):
                print(f"路径 {name[7:]+'.LEFT_CC_MASK2.jpg'} 不存在，跳过")
            else:
                onemaskpath2=os.path.join(path,name[7:]+'.LEFT_CC_MASK2.jpg')
                onemaskpath22 = os.path.join(path, name[7:] + '.LEFT_CC.jpg')
                txtname = name + '.LEFT_CC2'
                out_path=os.path.join(out_patha,'LEFT_CC2.jpg')
                cv2.imwrite(out_path,mydrawnote(onemaskpath2,onemaskpath22,txtname))


        if onepp == name[7:] + '.RIGHT_CC.jpg':
            if not os.path.exists(os.path.join(path, name[7:] + '.RIGHT_CC_Mask.jpg')):
                print(f"路径 {paths, name[7:] + '.RIGHT_CC_Mask.jpg'} 不存在，跳过")
            else:
                onemaskpath1 = os.path.join(path, name[7:] + '.RIGHT_CC_Mask.jpg')
                onemaskpath11 = os.path.join(path, name[7:] + '.RIGHT_CC.jpg')
                txtname = name + '.RIGHT_CC'
                out_path=os.path.join(out_patha,'RIGHT_CC.jpg')
                cv2.imwrite(out_path,mydrawnote(onemaskpath1,onemaskpath11,txtname))

            if not os.path.exists(os.path.join(path, name[7:] + '.RIGHT_CC_MASK2.jpg')):
                print(f"路径 {paths, name[7:] + '.RIGHT_CC_MASK2.jpg'} 不存在，跳过")
            else:
                onemaskpath2 = os.path.join(path, name[7:] + '.RIGHT_CC_MASK2.jpg')
                onemaskpath22 = os.path.join(path, name[7:] + '.RIGHT_CC.jpg')
                txtname = name + '.RIGHT_CC2'
                out_path=os.path.join(out_patha,'RIGHT_CC2.jpg')
                cv2.imwrite(out_path,mydrawnote(onemaskpath2,onemaskpath22,txtname))

        if onepp == name[7:] + '.LEFT_MLO.jpg':  # or onepp==name[7:]+'.RIGHT_CC.jpg':#MLOtest
            if not os.path.exists(os.path.join(path, name[7:] + '.LEFT_MLO_Mask.jpg')):
                print(f"路径 {paths, name[7:] + '.LEFT_MLO_Mask.jpg'} 不存在，跳过")
            else:
                onemaskpath1 = os.path.join(path, name[7:] + '.LEFT_MLO_Mask.jpg')
                onemaskpath11 = os.path.join(path, name[7:] + '.LEFT_MLO.jpg')
                txtname = name + '.LEFT_MLO'
                out_path=os.path.join(out_patha,'LEFT_MLO.jpg')
                cv2.imwrite(out_path,mydrawnote(onemaskpath1,onemaskpath11,txtname))

            if not os.path.exists(os.path.join(path, name[7:] + '.LEFT_MLO_MASK2.jpg')):
                print(f"路径 {paths, name[7:] + '.LEFT_MLO_MASK2.jpg'} 不存在，跳过")
            else:
                onemaskpath2 = os.path.join(path, name[7:] + '.LEFT_MLO_MASK2.jpg')
                onemaskpath22 = os.path.join(path, name[7:] + '.LEFT_MLO.jpg')
                txtname = name + '.LEFT_MLO2'
                out_path=os.path.join(out_patha,'LEFT_MLO2.jpg')
                cv2.imwrite(out_path,mydrawnote(onemaskpath2,onemaskpath22,txtname))

        if onepp == name[7:] + '.RIGHT_MLO.jpg':
            if not os.path.exists(os.path.join(path, name[7:] + '.RIGHT_MLO_Mask.jpg')):
                print(f"路径 {paths, name[7:] + '.RIGHT_MLO_Mask.jpg'} 不存在，跳过")
            else:
                onemaskpath1 = os.path.join(path, name[7:] + '.RIGHT_MLO_Mask.jpg')
                onemaskpath11 = os.path.join(path, name[7:] + '.RIGHT_MLO.jpg')
                txtname = name + '.RIGHT_MLO'
                out_path=os.path.join(out_patha,'RIGHT_MLO.jpg')
                cv2.imwrite(out_path,mydrawnote(onemaskpath1,onemaskpath11,txtname))

            if not os.path.exists(os.path.join(path, name[7:] + '.RIGHT_MLO_MASK2.jpg')):
                print(f"路径 {paths, name[7:] + '.RIGHT_MLO_MASK2.jpg'} 不存在，跳过")
            else:
                onemaskpath2 = os.path.join(path, name[7:] + '.RIGHT_MLO_MASK2.jpg')
                onemaskpath22 = os.path.join(path, name[7:] + '.RIGHT_MLO.jpg')
                txtname = name + '.RIGHT_MLO2'
                out_path=os.path.join(out_patha,'RIGHT_MLO2.jpg')
                cv2.imwrite(out_path,mydrawnote(onemaskpath2,onemaskpath22,txtname))

            #print(onepp)
