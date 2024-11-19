import os

# Đường dẫn tới thư mục chứa các file .txt
directory = 'D:/NTD/HUST/Ky_2024_1/Project1/DataNew/Wrench/train/labels'

# Hàm để sửa class_id trong file txt
def update_class_ids(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(file_path, 'w') as f:
        for line in lines:
            parts = line.strip().split()
            if parts:
                # Chuyển class_id từ 0 thành 1
                if parts[0] == '0':
                    parts[0] = '11'
                f.write(' '.join(parts) + '/n')

# Duyệt qua tất cả các file .txt trong thư mục
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        update_class_ids(file_path)

print("Đã cập nhật class_id trong các file .txt.")
