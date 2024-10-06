from PIL import Image
import pydicom
import pydicom.uid
import numpy as np
import os

def create_dicom_image(input_png_path, output_dcm_path):
    img = Image.open(input_png_path).convert('L')  # 转换为灰度图像
    img_array = np.array(img)

    dicom_dataset = pydicom.Dataset()

    # 设置DICOM文件的元数据和像素数据
    dicom_dataset.PhotometricInterpretation = "MONOCHROME2"
    dicom_dataset.SamplesPerPixel = 1
    dicom_dataset.PixelRepresentation = 0
    dicom_dataset.HighBit = img_array.dtype.itemsize * 8 - 1
    dicom_dataset.BitsStored = img_array.dtype.itemsize * 8
    dicom_dataset.BitsAllocated = img_array.dtype.itemsize * 8
    dicom_dataset.Rows = img_array.shape[0]
    dicom_dataset.Columns = img_array.shape[1]
    dicom_dataset.PixelData = img_array.tobytes()

    # 设置一些必须的DICOM文件头信息
    dicom_dataset.file_meta = pydicom.Dataset()
    dicom_dataset.file_meta.MediaStorageSOPClassUID = pydicom.uid.SecondaryCaptureImageStorage
    dicom_dataset.file_meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
    dicom_dataset.file_meta.ImplementationClassUID = pydicom.uid.generate_uid()
    dicom_dataset.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian

    # 设置患者信息和图像信息
    dicom_dataset.PatientName = "Patient^Name"
    dicom_dataset.PatientID = "123456"
    dicom_dataset.Modality = "OT"
    dicom_dataset.SeriesInstanceUID = pydicom.uid.generate_uid()
    dicom_dataset.StudyInstanceUID = pydicom.uid.generate_uid()
    dicom_dataset.FrameOfReferenceUID = pydicom.uid.generate_uid()

    dicom_dataset.save_as(output_dcm_path)

def batch_convert_png_to_dicom(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(source_dir, filename)
            output_path = os.path.join(target_dir, os.path.splitext(filename)[0] + '.dcm')
            create_dicom_image(input_path, output_path)
            print(f"Converted {filename} to DICOM.")


source_directory = r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\one\resize_redeal\org\mini\all_images_dtext'
target_directory = r'D:\sjwlab\meixuewen\all_data\our_data\ddsm-mini\afterdeal_mini\one\dicom_files'

batch_convert_png_to_dicom(source_directory, target_directory)
