# import os
#
# filepath= r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-cbis\afterdeal_cbis\one\all_labels'
#
#
# # with open(filename, 'r') as file:
# #     content = file.read()
# #
# # # 将内容按空格分割成列表
# # numbers = content.split()
# #
# # # 确保列表至少有两个元素
# # if len(numbers) >= 2:
# #     # 取最后两个元素，并转换为整数
# #     a = numbers[-2]
# #     b = numbers[-1]
# # else:
# #     print("文件中的数字不足两个。")
# #
# # print(a,b)
#
# def qulasttwo(filename):
#     with open(filename, 'r') as file:
#         content = file.read()
#
#     # 将内容按空格分割成列表
#     numbers = content.split()
#
#     # 确保列表至少有两个元素
#     if len(numbers) >= 2:
#         # 取最后两个元素，并转换为整数
#         a = numbers[-2]
#         b = numbers[-1]
#     else:
#         print("文件中的数字不足两个。")
#     return a,b
#
# maxa=0.0
# maxb=0.0
# for file in os.listdir(filepath):
#     txtpath=os.path.join(filepath,file)
#     fa,fb=qulasttwo(txtpath)
#     if float(fa)>maxa:
#         maxa=fa
#     if float(fb)>maxb:
#         maxb=fb
#
# print('maxa,maxb:',maxa,maxb)



import os
import cv2

def resize_image(img, output_size=(600, 800)):

    if img is None:
        raise ValueError("无法读取图像或路径不正确")

    width, height = output_size
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    return resized_img

filepath = r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\two\yolo_data_pure\labels\all_labels'

def qulasttwo(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # 将内容按空格分割成列表
    numbers = content.split()

    # 确保列表至少有两个元素
    if len(numbers) >= 2:
        # 取最后两个元素，并转换为整数
        d = numbers[-4]
        c = numbers[-3]
        a = numbers[-2]
        b = numbers[-1]
    else:
        print("文件中的数字不足两个。")
    return d,c,a, b

maxa, maxb = 0.0, 0.0  # 使用浮点数初始化
for file in os.listdir(filepath):
    txtpath = os.path.join(filepath, file)
    fd,fc,fa, fb = qulasttwo(txtpath)
    fd=float(fd)
    fc=float(fc)
    fa=float(fa)
    fb=float(fb)
    if (fa)<0.045and (fb)<0.045:
        if (fa) > maxa:
                maxa = (fa)
                b1=fb
                c1=fc
                d1=fd
                aname=file
        if (fb) > maxb:
                maxb = (fb)
                a2=fa
                c2=fc
                d2=fd
                bname=file
print('maxa, maxb:', maxa, maxb)
print(aname,bname)


a,b,c,d=d1,c1,maxa, b1
print(a, b,c,d)
image_path = r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\two\yolo_data_pure\images\all_images'
im1p=os.path.join(image_path,aname[:-4]+'.jpg')
image = cv2.imread(im1p,0)
h,w=image.shape
# print(h,w)
a=a*w
b=b*h
c=c*w
d=d*h

# 计算矩形的左上角和右下角坐标
left_top = (int(a - c / 2), int(b - d / 2))
right_bottom = (int(a + c / 2), int(b + d / 2))

# 在图像上绘制矩形
cv2.rectangle(image, left_top, right_bottom, (255, 255, 0), 3)

# 显示结果
cv2.imshow('Rectangle', resize_image(image))
cv2.waitKey(0)
cv2.destroyAllWindows()





