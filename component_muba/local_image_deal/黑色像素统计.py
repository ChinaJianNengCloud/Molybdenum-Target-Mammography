from PIL import Image
import os


image_folder = r'D:\wuwei\Meixw\second_data\minideal2\f_images2'

total_images = 0
black_pixel_images = 0
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        total_images += 1
        image_path = os.path.join(image_folder, filename)
        image = Image.open(image_path).convert('L')  # 转换为灰度图像！！！！！
        pixels = image.load()
        width, height = image.size
        total_pixels = width * height
        black_pixels = sum(pixels[x, y] < 16 for x in range(width) for y in range(height))  # 16是灰度值的一个阈值

        if black_pixels / total_pixels >= 0.96:
            black_pixel_images += 1


print(f"Total images: {total_images}")
print(f"Images with black pixels >= 95%: {black_pixel_images}")
