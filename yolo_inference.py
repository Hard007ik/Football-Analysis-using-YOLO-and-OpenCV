from ultralytics import YOLO

model = YOLO("best.pt") # load trained model
results = model.predict("input_video/challenge-1140_1.mp4", save=True)
print(results[0])
print("="*20)

for box in results[0].boxes:
    print(box)