Cell 1
# Convolutional Neural Networks (CNN)
This notebook explores the basics of CNNs and their applications in image-related tasks.

----------------------------------------
Cell 2
## Why CNNs?

CNNs are designed specifically for image processing.

Applications:

- Object Detection
- Face Recognition
- Medical Imaging
- Defect Detection
- Quality Inspection

----------------------------------------                          
Cell 3
applications = [
    "Object Detection",
    "Face Recognition",
    "Defect Detection",
    "Quality Inspection"
]

for app in applications:
    print(app)

----------------------------------------
Cell 4
## Components of CNN

1. Convolution Layer
2. Activation Function
3. Pooling Layer
4. Flatten Layer
5. Fully Connected Layer

----------------------------------------
Cell 5
cnn_layers = [
    "Convolution",
    "ReLU",
    "Pooling",
    "Flatten",
    "Dense"
]

for layer in cnn_layers:
    print(layer)

----------------------------------------
Cell 6
## Sample CNN Architecture

----------------------------------------
Cell 7
import tensorflow as tf

cnn_model = tf.keras.Sequential([

    tf.keras.layers.Conv2D(
        32,
        (3,3),
        activation='relu',
        input_shape=(64,64,3)
    ),

    tf.keras.layers.MaxPooling2D((2,2)),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(
        64,
        activation='relu'
    ),

    tf.keras.layers.Dense(
        2,
        activation='softmax'
    )

])

cnn_model.summary()

----------------------------------------
Cell 8
## Industrial Quality Assurance

CNNs can be used to analyze product images and automatically detect defects such as:

- Scratches
- Cracks
- Surface Damage
- Missing Components

This makes them highly useful in industrial quality inspection systems.

----------------------------------------
Cell 9
product_images = [
    "Image_1",
    "Image_2",
    "Image_3"
]

for image in product_images:
    print(image, "-> Sent for CNN Inspection")
