import os

# Đường dẫn đến thư mục chứa dữ liệu
data_dir = 'D:/NTD/HUST/Ky_2024_1/Project1/DataTrainYOLO/Datanew/dataset/datafull/val'
labels_dir = os.path.join(data_dir, 'labels')
images_dir = os.path.join(data_dir, 'images')

# Lấy danh sách các tệp ảnh
image_files = {f.replace('.jpg', '') for f in os.listdir(images_dir) if f.endswith('.jpg')}

# Lấy danh sách các tệp nhãn
label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

for label_file in label_files:
    label_name = label_file.replace('.txt', '')
    
    # Kiểm tra nếu không có tệp jpg tương ứng
    if label_name not in image_files:
        label_path = os.path.join(labels_dir, label_file)
        os.remove(label_path)
        print(f"Đã xóa tệp nhãn không có tệp ảnh tương ứng: {label_file}")

print("Hoàn tất xóa các tệp nhãn không có tệp ảnh tương ứng!")
