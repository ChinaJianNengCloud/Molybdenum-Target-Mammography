// 设置自动阈值方法为Huang dark
setAutoThreshold("Huang dark");

// 设置图像背景为黑色
setOption("BlackBackground", true);

// 将图像转换为二值掩膜
run("Convert to Mask");

// 去除图像中的斑点噪声
run("Despeckle");

// 移除亮色异常值
run("Remove Outliers...", "radius=3 threshold=50 which=Bright");

// 填充图像中的孔洞
run("Fill Holes");

// 对图像进行膨胀操作，重复多次以增强效果
run("Dilate");
run("Dilate");
run("Dilate");
run("Dilate");
run("Dilate");
run("Dilate");

// 获取当前图像的标题（不包括扩展名）
baseName = getTitle();

// 获取当前图像的目录
inputDir = getDirectory("image");

// 设置输出目录，确保这个目录存在
// 使用双反斜杠进行转义
outputDir = "D:\\sjwlab\\meixuewen\\all_data\\our_data\\ZMeixwtiqu\\all_data\\mini\\all_images_redeal_de2\\";

// 或者使用正斜杠
// outputDir = "D:/sjwlab/meixuewen/all_data/our_data/ZMeixwtiqu/all_data/mini/all_images_redeal_de2/";

// 构建新的文件名，使用原始文件名并在其后添加 "_processed"（或你选择的任何后缀）
saveName = outputDir + baseName + "_processed.png";

// 保存处理后的图像，这里假设你想要保存为TIFF格式
// 注意：文件扩展名应该与保存格式一致，所以如果保存为TIFF，扩展名应该是 ".tif"
saveAs("TIFF", saveName);
