import streamlit as st
from ultralytics import YOLO
import tempfile
import ollama
from datetime import datetime

# Page Title
st.title("AI-Powered Industrial Quality Assurance System")

# User Inputs
inspector_name = st.text_input("Inspector Name")

project_location = st.text_input("Project Location")

project_id = st.text_input("Project ID")

# Image Upload
uploaded_file = st.file_uploader(
    "Upload a steel surface image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Display uploaded image
    st.subheader("Uploaded Image")
    st.image(uploaded_file, use_container_width=True)

    st.subheader("Running Defect Detection...")

    # Load YOLO model
    model = YOLO("best.pt")

    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.read())
        image_path = tmp_file.name

    # Run YOLO prediction
    results = model(image_path)

    st.subheader("Detected Defects")

    found_defects = []

    for result in results:
        for box in result.boxes:

            cls_id = int(box.cls[0])

            defect_name = model.names[cls_id]

            found_defects.append(defect_name)

    # Remove duplicate defects
    found_defects = list(set(found_defects))

    if found_defects:

        # Show defects
        for defect in found_defects:
            st.write(f"• {defect}")

        # Current date
        today = datetime.now().strftime("%d %B %Y")

        # Convert defects to text
        defect_text = "\n".join(
            f"• {defect}" for defect in found_defects
        )

        # Prompt for Llama
        prompt = f"""
Generate a professional steel inspection report.

Inspection Date: {today}
Inspector Name: {inspector_name}
Project Location: {project_location}
Project ID: {project_id}

Detected Defects:
{defect_text}

Requirements:
- Use the Inspection Date provided above
- Use the Inspector Name provided above
- Use the Project Location provided above
- Use the Project ID provided above
- Do NOT use placeholders such as [Insert Name]
- Do NOT ask for missing information
- Include:
  1. Inspection Date
  2. Inspector Name
  3. Project Location
  4. Project ID
  5. Detected Defects
  6. Summary
  7. Severity
  8. Recommended Actions
- Keep the report professional and concise
"""

        st.subheader("Generating AI Inspection Report...")

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.subheader("Inspection Report")

        st.write(response["message"]["content"])

    else:

        st.success("No defects detected.")