print("HELLO FROM COMBINED TEST")

from ultralytics import YOLO
import ollama

print("STEP 1")

model = YOLO("best.pt")

print("STEP 2")

results = model("train_batch0.jpg")

print("STEP 3")

detected_defects = []

for result in results:
    for box in result.boxes:
        cls_id = int(box.cls[0])
        confidence = float(box.conf[0])

        detected_defects.append(
            f"{model.names[cls_id]} ({confidence*100:.1f}%)"
        )

print("STEP 4")
print(detected_defects)

defect_text = "\n".join(
    f"- {d}" for d in detected_defects
)

prompt = f"""
Generate a professional steel inspection report.

Detected Defects:
{defect_text}

Include:
1. Summary
2. Severity
3. Recommended Actions
"""

print("STEP 5 - Calling Ollama")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("STEP 6 - Ollama returned")

print(response["message"]["content"])