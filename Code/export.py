from ultralytics import YOLO

model = YOLO("yolov8x.pt")  
model = YOLO("D:/NTD/HUST/Ky_2024_1/Project1/Model_Yolov8x/runs/detect/train/weights/best.pt") 

model.export(format="onnx")