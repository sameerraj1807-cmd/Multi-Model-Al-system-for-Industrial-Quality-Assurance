Cell 1
# Week 3 - Deep Learning Fundamentals

This notebook contains my notes and practice code on Deep Learning concepts learned during Week 3.

----------------------------------------
Cell 2
## What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses Artificial Neural Networks with multiple layers to learn complex patterns from data.

----------------------------------------
Cell 3
print("Deep Learning helps computers learn complex patterns from large amounts of data.")

----------------------------------------
Cell 4
## Artificial Neural Networks (ANN)

A neural network consists of:

- Input Layer
- Hidden Layer(s)
- Output Layer

Neurons in each layer process information and pass it to the next layer.

----------------------------------------
Cell 5
input_layer = 4
hidden_layer = 8
output_layer = 1

print("Input Layer:", input_layer)
print("Hidden Layer:", hidden_layer)
print("Output Layer:", output_layer)

----------------------------------------
Cell 6
## Activation Functions

Activation functions help neural networks learn non-linear patterns.

Common activation functions:

- ReLU
- Sigmoid
- Tanh

----------------------------------------
Cell 7
import numpy as np

x = [-2, -1, 0, 1, 2]

relu = [max(0, value) for value in x]

print("Input:", x)
print("ReLU Output:", relu)

----------------------------------------
Cell 8
## Building a Simple Neural Network using TensorFlow

----------------------------------------
Cell 9
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

----------------------------------------
Cell 10
## Key Learning

Neural networks learn patterns by adjusting weights during training using backpropagation and o
