# import torch
# from torch.utils.data import DataLoader, TensorDataset
# from vit_pytorch import ViT
#
# # 假设数据集大小为 10000 个样本，每个样本是一个 3 通道的 256x256 图像
# num_samples = 100
# image_size = 256
# channels = 3
# num_classes = 10  # 假设有 10 个不同的类别
#
# 
# images = torch.randn(num_samples, channels, image_size, image_size)
# labels = torch.randint(low=0, high=num_classes, size=(num_samples,))
#
# 
# dataset = TensorDataset(images, labels)
# dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
#
# 
# model = ViT(
#     image_size=image_size,
#     patch_size=32,
#     num_classes=num_classes,
#     dim=1024,
#     depth=6,
#     heads=8,
#     mlp_dim=2048
# )
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# model.to(device)
# 
# criterion = torch.nn.CrossEntropyLoss()
#
# 
# optimizer = torch.optim.Adam(model.parameters(), lr=3e-4)
#
# 
# num_epochs = 10 
# for epoch in range(num_epochs):
#     for i, (images, labels) in enumerate(dataloader):
#         images, labels = images.to(device), labels.to(device)
#         outputs = model(images)
#         loss = criterion(outputs, labels)
#
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
#
#         if (i + 1) % 1 == 0:
#             print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(dataloader)}], Loss: {loss.item():.4f}')
#
# torch.save(model.state_dict(), 'pretrained-net.pth')

import torch
from torch.utils.data import DataLoader, TensorDataset
from vit_pytorch import ViT

# 假设数据集大小为 10000 个样本，每个样本是一个 3 通道的 256x256 图像
num_samples = 100
image_size = 256
channels = 3
num_classes = 10  # 假设有 10 个不同的类别

# 生成随机图像和标签
images = torch.randn(num_samples, channels, image_size, image_size)
labels = torch.randint(low=0, high=num_classes, size=(num_samples,))

# 创建一个 TensorDataset 和 DataLoader
dataset = TensorDataset(images, labels)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# 创建 ViT 模型
model = ViT(
    image_size=image_size,
    patch_size=32,
    num_classes=num_classes,
    dim=1024,
    depth=6,
    heads=8,
    mlp_dim=2048
)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)
criterion = torch.nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=3e-4)


num_epochs = 10 
for epoch in range(num_epochs):
    total_loss = 0.0 
    for i, (images, labels) in enumerate(dataloader):
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        total_loss += loss.item()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    average_loss = total_loss / len(dataloader)
    print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {average_loss:.4f}')

torch.save(model.state_dict(), 'pretrained-net.pth')
