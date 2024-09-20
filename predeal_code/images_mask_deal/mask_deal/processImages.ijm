// �����Զ���ֵ����ΪHuang dark
setAutoThreshold("Huang dark");

// ����ͼ�񱳾�Ϊ��ɫ
setOption("BlackBackground", true);

// ��ͼ��ת��Ϊ��ֵ��Ĥ
run("Convert to Mask");

// ȥ��ͼ���еİߵ�����
run("Despeckle");

// �Ƴ���ɫ�쳣ֵ
run("Remove Outliers...", "radius=3 threshold=50 which=Bright");

// ���ͼ���еĿ׶�
run("Fill Holes");

// ��ͼ��������Ͳ������ظ��������ǿЧ��
run("Dilate");
run("Dilate");
run("Dilate");
run("Dilate");
run("Dilate");
run("Dilate");

// ��ȡ��ǰͼ��ı��⣨��������չ����
baseName = getTitle();

// ��ȡ��ǰͼ���Ŀ¼
inputDir = getDirectory("image");

// �������Ŀ¼��ȷ�����Ŀ¼����
// ʹ��˫��б�ܽ���ת��
outputDir = "D:\\sjwlab\\meixuewen\\all_data\\our_data\\ZMeixwtiqu\\all_data\\mini\\all_images_redeal_de2\\";

// ����ʹ����б��
// outputDir = "D:/sjwlab/meixuewen/all_data/our_data/ZMeixwtiqu/all_data/mini/all_images_redeal_de2/";

// �����µ��ļ�����ʹ��ԭʼ�ļ������������� "_processed"������ѡ����κκ�׺��
saveName = outputDir + baseName + "_processed.png";

// ���洦����ͼ�������������Ҫ����ΪTIFF��ʽ
// ע�⣺�ļ���չ��Ӧ���뱣���ʽһ�£������������ΪTIFF����չ��Ӧ���� ".tif"
saveAs("TIFF", saveName);
