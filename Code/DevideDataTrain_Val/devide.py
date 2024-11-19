import os
import random
import shutil

# Đường dẫn đến thư mục chứa dữ liệu
data_dir = 'D:/NTD/HUST/Ky_2024_1/Project1/DataTrainYOLO/Datanew/dataset/datafull'
images_dir = os.path.join(data_dir, 'images')
labels_dir = os.path.join(data_dir, 'labels')

# Tạo thư mục cho train và val nếu chưa tồn tại
os.makedirs(os.path.join(data_dir, 'train/images'), exist_ok=True)
os.makedirs(os.path.join(data_dir, 'train/labels'), exist_ok=True)
os.makedirs(os.path.join(data_dir, 'val/images'), exist_ok=True)
os.makedirs(os.path.join(data_dir, 'val/labels'), exist_ok=True)

# Lấy danh sách các tệp ảnh và nhãn
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

# Kiểm tra tính đồng nhất giữa ảnh và nhãn
assert len(image_files) == len(label_files), "Số lượng ảnh và nhãn không khớp!"

# Xáo trộn danh sách tệp
random.shuffle(image_files)

# Chia tệp thành tập train và val
split_index = int(len(image_files) * 0.8)
train_images = image_files[:split_index]
val_images = image_files[split_index:]

# Di chuyển tệp vào thư mục tương ứng
for img in train_images:
    shutil.copy(os.path.join(images_dir, img), os.path.join(data_dir, 'train/images', img))
    label_file = img.replace('.jpg', '.txt')
    shutil.copy(os.path.join(labels_dir, label_file), os.path.join(data_dir, 'train/labels', label_file))

for img in val_images:
    shutil.copy(os.path.join(images_dir, img), os.path.join(data_dir, 'val/images', img))
    label_file = img.replace('.jpg', '.txt')
    shutil.copy(os.path.join(labels_dir, label_file), os.path.join(data_dir, 'val/labels', label_file))

print("Chia tệp thành công!")
