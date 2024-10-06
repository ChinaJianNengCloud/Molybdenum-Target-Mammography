import os
import cv2

imfile_path=r'D:\sjwlab\meixuewen\all_data\our_data\DMID\DMID_afterdead\two\DMID_images'
# minh,minw=999999999999,99999999999999
# maxh,maxw=0,0
for I in os.listdir(imfile_path):
    ipath=os.path.join(imfile_path,I)
    minh, minw = 999999999999, 99999999999999
    maxh, maxw = 0, 0
    for imfile in os.listdir(ipath):
        im_path=os.path.join(ipath,imfile)
        img=cv2.imread(im_path,0)
        height, width = img.shape
        f=height*width
        if f>maxh*maxw:
            maxw=width
            maxh=height
        if f<minw*minh:
            minh=height
            minw=width

    print('max: ',maxh,maxw)
    print('min: ',minh,minw)



#####多线程,单层

# import os
# import cv2
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import threading
#
# # 创建一个锁对象
# lock = threading.Lock()
#
# imfile_path = r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\all_data\inbreast\all_images'
# minh, minw = 999999999999, 999999999999
# maxh, maxw = 0, 0
#
#
# # 定义一个函数来处理单个图像文件
# def process_image(imfile):
#     global minh, minw, maxh, maxw
#     im_path = os.path.join(imfile_path, imfile)
#     img = cv2.imread(im_path, 0)
#     height, width = img.shape
#
#     with lock:  # 在这里获取锁
#         f = height * width
#         if f > maxh * maxw:
#             maxw = width
#             maxh = height
#         if f < minw * minh:
#             minh = height
#             minw = width
#
#
# # 获取文件列表
# image_files = [f for f in os.listdir(imfile_path) if os.path.isfile(os.path.join(imfile_path, f))]
#
# # 使用ThreadPoolExecutor创建一个线程池
# with ThreadPoolExecutor(max_workers=4) as executor:
#     # 提交任务到线程池
#     futures = {executor.submit(process_image, imfile): imfile for imfile in image_files}
#     # 等待所有任务完成
#     for future in as_completed(futures):
#         # 这里可以捕获异常或处理结果
#         pass
#
# print('max: ', maxh, maxw)
# print('min: ', minh, minw)