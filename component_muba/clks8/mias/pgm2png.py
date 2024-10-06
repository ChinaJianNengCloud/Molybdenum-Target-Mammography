# import os
#
# from PIL import Image
#
# def pgm_to_png(pgm_file, png_file):
#     # 打开PGM文件
#     with Image.open(pgm_file) as img:
#         # 将图像保存为PNG格式
#         img.save(png_file, 'PNG')
#
# # # 使用函数
# # pgm_to_png(r'D:\sjwlab\meixuewen\all_data\our_data\mias\org_mias\all-mias\mdb003.pgm', 'output.png')
#
# pgmpath=r'D:\sjwlab\meixuewen\all_data\our_data\mias\org_mias\all-mias'
# outpath=r'D:\sjwlab\meixuewen\all_data\our_data\mias\afterdeal_mias\test'
#
# for pgmfile in os.listdir(pgmpath):
#     if pgmfile.endswith('.pgm'):
#         pgmpath=os.path.join(pgmpath,pgmfile)
#         out=os.path.join(outpath,pgmfile[:-4]+'.png')
#         pgm_to_png(pgmpath,out)
#
#
import os
from PIL import Image


def pgm_to_png(pgm_file, png_file):
    # 打开PGM文件
    with Image.open(pgm_file) as img:
        # 将图像保存为PNG格式
        img.save(png_file, 'PNG')


pgmpath = r'D:\sjwlab\meixuewen\all_data\our_data\mias\org_mias\all-mias'
outpath = r'D:\sjwlab\meixuewen\all_data\our_data\mias\afterdeal_mias\test'

# 遍历PGM文件夹中的所有文件
for pgmfile in os.listdir(pgmpath):
    if pgmfile.endswith('.pgm'):
        # 构建完整的PGM文件路径
        pgm_full_path = os.path.join(pgmpath, pgmfile)
        # 构建输出的PNG文件路径
        png_full_path = os.path.join(outpath, pgmfile[:-4] + '.png')

        # 调用函数转换文件
        pgm_to_png(pgm_full_path, png_full_path)

print("转换完成！")