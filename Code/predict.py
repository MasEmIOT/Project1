from ultralytics import YOLO

model = YOLO("yolo11m.pt")  
model = YOLO("D:/NTD/HUST/Ky_2024_1/Project1/Yolo11mNew/runs/detect/train/weights/best.pt")

# results = model.predict(show=True,source="D:/NTD/HUST/Ky_2024_1/Project1/Precdict/TestDataa/2e265e55-037c-4382-ac34-c339d628f38b.jpg")
results = model("D:/NTD/HUST/Ky_2024_1/Project1/Precdict/TestDataa/b8977600-b826-424e-9fd0-d0f393c83fae.jpg")  # predict on an image
print(results)
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk