from ultralytics import YOLO

model = YOLO("best.pt")

results = model("train_batch0.jpg")

print("\nDetected Defects:\n")

for result in results:
    for box in result.boxes:
        cls_id = int(box.cls[0])
        confidence = float(box.conf[0])

        print(
            f"• {model.names[cls_id]} "
            f"({confidence*100:.1f}%)"
        )