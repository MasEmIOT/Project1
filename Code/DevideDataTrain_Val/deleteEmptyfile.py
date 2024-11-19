import os

# Đường dẫn đến thư mục chứa dữ liệu
data_dir = 'D:/NTD/HUST/Ky_2024_1/Project1/DataTrainYOLO/Datanew/dataset/datafull/val'
labels_dir = os.path.join(data_dir, 'labels')
train_images_dir = os.path.join(data_dir, 'images')

# Lấy danh sách các tệp nhãn
label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

for label_file in label_files:
    label_path = os.path.join(labels_dir, label_file)
    
    # Kiểm tra xem tệp nhãn có rỗng không
    if os.path.getsize(label_path) == 0:
        # Xóa tệp nhãn rỗng
        os.remove(label_path)
        print(f"Đã xóa tệp nhãn rỗng: {label_file}")
        
        # Tìm tệp ảnh tương ứng và xóa nếu tồn tại
        image_file = label_file.replace('.txt', '.jpg')
        image_path = os.path.join(train_images_dir, image_file)
        
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Đã xóa tệp ảnh tương ứng: {image_file}")

print("Hoàn tất xóa các tệp không có giá trị!")
