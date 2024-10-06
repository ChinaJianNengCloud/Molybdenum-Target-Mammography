import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os
import torch.nn as nn
import numpy as np
import torch.optim as optim
from torchvision import models
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score

testloss = []
trainloss = []
epochs = []
train_acc = []
test_auc = []
test_acc = []


class CustomImageDataset(Dataset):
    def __init__(self, images_path, labels_path, transform=None):
        self.images_path = images_path
        self.labels_path = labels_path
        self.transform = transform
        self.images_names = sorted(
            [f for f in os.listdir(images_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    def __len__(self):
        return len(self.images_names)

    def __getitem__(self, idx):
        img_name = self.images_names[idx]
        img_path = os.path.join(self.images_path, img_name)
        image = Image.open(img_path)

        file_base, file_extension = os.path.splitext(img_name)
        label_name = file_base + '_label.txt'
        label_path = os.path.join(self.labels_path, label_name)

        with open(label_path, 'r') as f:
            label_str = f.read().strip()

            label = int(label_str.split()[0])

        if self.transform:
            image = self.transform(image)
        return image, label


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

train_dataset = CustomImageDataset(images_path=r'D:\wuwei\Meixw\fimages\processed_images_train',
                                   labels_path=r'D:\wuwei\Meixw\flabels\labels_train',
                                   transform=transform)

test_dataset = CustomImageDataset(images_path=r'D:\wuwei\Meixw\fimages\processed_images_val',
                                  labels_path=r'D:\wuwei\Meixw\flabels\labels_val',
                                  transform=transform)

test_data_loader = DataLoader(test_dataset, batch_size=256, shuffle=True)

train_data_loader = DataLoader(train_dataset, batch_size=256, shuffle=True)
for batch_idx, (images, labels) in enumerate(train_data_loader):
    print(f"Batch {batch_idx}:")

print('done!')

resnet = models.resnet101(pretrained=True)

num_ftrs = resnet.fc.in_features
num_classes = 3
new_fc = nn.Linear(num_ftrs, num_classes)

resnet.fc = new_fc

# class_weights = torch.tensor([5.2, 6.5,1.5])
# class_weights = torch.tensor([1.8, 2.24, 1])
# class_weights = class_weights.to('cuda' if torch.cuda.is_available() else 'cpu')
# criterion = nn.CrossEntropyLoss(
#                                 #weight=class_weights
#                                 )


# optimizer = torch.optim.Adam(resnet.parameters(), lr=0.001)

if torch.cuda.device_count() > 1:
    resnet = nn.DataParallel(resnet)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(resnet.parameters(), lr=0.001)

# 将模型移动到GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
resnet.to(device)
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# resnet.to(device)

trainloss, train_acc, testloss, test_acc = [], [], [], []
test_acc_per_class = [[] for _ in range(num_classes)]

num_epochs = 200
for epoch in range(num_epochs):
    resnet.train()
    running_loss = 0.0
    correct_train = 0
    total_train = 0
    for batch_idx, (inputs, labels) in enumerate(train_data_loader):
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = resnet(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total_train += labels.size(0)
        correct_train += (predicted == labels).sum().item()

    average_train_loss = running_loss / len(train_data_loader)
    trainloss.append(average_train_loss)
    train_accuracy = correct_train / total_train
    train_acc.append(train_accuracy)

    # 测试阶段
    resnet.eval()
    class_correct = [0 for _ in range(num_classes)]
    class_total = [0 for _ in range(num_classes)]
    test_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_data_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = resnet(inputs)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
            c = (predicted == labels).squeeze()
            for i in range(len(labels)):
                label = labels[i]
                class_correct[label] += c[i].item()
                class_total[label] += 1

    test_acc_per_class_epoch = [class_correct[i] / class_total[i] if class_total[i] > 0 else 0 for i in
                                range(num_classes)]

    for i in range(num_classes):
        test_acc_per_class[i].append(test_acc_per_class_epoch[i])

    average_test_loss = test_loss / len(test_data_loader)
    testloss.append(average_test_loss)
    accuracy = correct / total
    test_acc.append(accuracy)
    epochs.append(epoch)
    print(f'Finished Epoch {epoch + 1}')
model_save_path = 'orgmodel101.pth'
torch.save(resnet, model_save_path)
print('Training and evaluation completed!')

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(epochs, test_acc, marker=',', color='b', label='test_acc')
plt.plot(epochs, train_acc, marker=',', color='g', label='train_acc')
# plt.plot(epochs, test_auc, marker=',', color='r', label='test_auc')
plt.xlabel('Epoch')
plt.ylabel('Acc')
plt.title('Acc vs Epoch')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(epochs, trainloss, marker=',', color='b', label='trainloss')
plt.plot(epochs, testloss, marker=',', color='g', label='testloss')
plt.xlabel('Epoch')
plt.ylabel('loss')
plt.title('loss vs Epoch')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 3)
for i in range(num_classes):
    plt.plot(epochs, test_acc_per_class[i], marker=',', label=f'Class {i} Test Acc')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Test Accuracy per Class vs Epoch')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
