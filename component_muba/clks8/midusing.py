# # import os
# # from pydicom import dcmread
# # from PIL import Image
# # import numpy as np
# #
# # dcm_file_path=r'F:\sjwlab\meixuewen\LIBRA-1.0.4\LIBRA-1.0.4\Sample_Data\Case3.dcm'
# #
# # ds = dcmread(dcm_file_path)
# # print(ds)
# #
# import os
#
# import pydicom
#
# def read_dicom_file(filename):
#     """读取DICOM文件"""
#     return pydicom.read_file(filename)
#
# def write_dicom_file(dataset, filename):
#     """将DICOM数据集写入文件"""
#     dataset.save_as(filename)
#
# def merge_datasets(baseline_dataset, incomplete_dataset):
#     """合并两个DICOM数据集，使用基线数据集中缺失的信息填补不完整数据集"""
#     for keyword in baseline_dataset.dir():
#         if keyword not in incomplete_dataset or (incomplete_dataset[keyword].VR != 'SQ' and not incomplete_dataset[keyword].value):
#             # 如果是序列（Sequence），则不自动填充，因为这可能涉及到复杂的逻辑
#             if keyword not in ['PixelData']:  # 如果需要复制像素数据，可以根据需求调整
#                 incomplete_dataset.add(baseline_dataset.data_element(keyword))
#     return incomplete_dataset
#
#
# # 主程序
# if __name__ == "__main__":
#     # 读取基准文件
#     baseline_dataset = read_dicom_file(r'F:\sjwlab\meixuewen\LIBRA-1.0.4\LIBRA-1.0.4\Sample_Data\Case3.dcm')
#
#     # 读取待补全文件
#     #incomplete_dataset = read_dicom_file(r'D:\sjwlab\meixuewen\all_data\our_data\CMMD\org_CMMD\CMMD\D1-0001\07-18-2010-NA-NA-79377\1.000000-NA-70244\1-2.dcm')
#     filepath=r'D:\sjwlab\meixuewen\all_data\our_data\ZMeixwtiqu\dcm_compared\local_duo'
#     for im in os.listdir(filepath):
#         inpath=os.path.join(filepath,im)
#     # 对比并补全
#         incomplete_dataset = read_dicom_file(inpath)
#         merged_dataset = merge_datasets(baseline_dataset, incomplete_dataset)
#
#         write_dicom_file(merged_dataset, inpath)



import os
import pydicom

def read_dicom_file(filename):
    """读取DICOM文件"""
    return pydicom.dcmread(filename)

def write_dicom_file(dataset, filename):
    """将DICOM数据集写入文件"""
    dataset.save_as(filename)

def merge_datasets(baseline_dataset, incomplete_dataset):
    """合并两个DICOM数据集，使用基线数据集中缺失的信息填补不完整数据集"""
    for keyword in baseline_dataset.dir():
        # 检查关键字是否在incomplete_dataset中，如果不在或者值为空，则添加
        if keyword not in incomplete_dataset or (incomplete_dataset[keyword].VR != 'SQ' and not incomplete_dataset[keyword].value):
            # 如果是序列（Sequence），则不自动填充，因为这可能涉及到复杂的逻辑
            if keyword not in ['PixelData']:  # 如果需要复制像素数据，可以根据需求调整
                # 复制元素而不是整个数据集
                data_element = baseline_dataset.data_element(keyword)
                # 必须使用 copy() 来复制数据元素，否则会有引用问题
                incomplete_dataset.add_new(data_element.tag, data_element.VR, data_element.value)
    return incomplete_dataset

# 主程序
if __name__ == "__main__":
    # 读取基准文件
    baseline_dataset = read_dicom_file(r'F:\sjwlab\meixuewen\LIBRA-1.0.4\LIBRA-1.0.4\Sample_Data\Case3.dcm')

    # 读取待补全文件的目录
    filepath=r'D:\sjwlab\meixuewen\all_data\our_data\libra\testin'
    for im in os.listdir(filepath):
        inpath = os.path.join(filepath, im)
        # 读取待补全文件
        incomplete_dataset = read_dicom_file(inpath)
        # 对比并补全
        merged_dataset = merge_datasets(baseline_dataset, incomplete_dataset)
        # 写入补全后的文件
        write_dicom_file(merged_dataset, inpath)
