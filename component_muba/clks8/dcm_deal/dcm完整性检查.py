import os
import pydicom
from pydicom.errors import InvalidDicomError

# 设定DICOM文件所在的目录
dicom_directory =r"D:\sjwlab\meixuewen\all_data\our_data\libra\testin"

# 必须的DICOM标签列表
required_tags = [
    'PatientID',
    'StudyDate',
    'SeriesDescription',
    'InstanceNumber',
    'SOPInstanceUID'
]

# 检查文件完整性的函数
def check_dicom_integrity(dicom_file):
    try:
        ds = pydicom.dcmread(dicom_file)
        for tag in required_tags:
            if tag not in ds:
                return False, f"Missing tag: {tag}"
        return True, "OK"
    except InvalidDicomError:
        return False, "Invalid DICOM file"

# 遍历目录中的所有文件
for root, dirs, files in os.walk(dicom_directory):
    for file in files:
        if file.lower().endswith(".dcm"):
            file_path = os.path.join(root, file)
            is_complete, message = check_dicom_integrity(file_path)
            print(f"{file_path}: {message}")

