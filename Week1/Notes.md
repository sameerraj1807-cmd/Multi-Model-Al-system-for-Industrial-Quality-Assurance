# Week 1 Notes - Python Basics

## What is Python?

Python is a high-level, interpreted programming language known for its simple syntax and readability. It is widely used in fields such as:

- Artificial Intelligence
- Machine Learning
- Data Science
- Web Development
- Automation

Python's simplicity makes it one of the best languages for beginners and one of the most popular languages in the AI industry.

---

## Why Python for AI and Machine Learning?

Python provides a large collection of libraries and tools that make AI development easier.

Some popular libraries include:

- NumPy
- Pandas
- Matplotlib
- Scikit-Learn
- TensorFlow
- PyTorch

These libraries help in data processing, visualization, machine learning, and deep learning tasks.

---

## Variables

Variables are used to store data values.

Example:

```python
name = "Sameer"
age = 19
```

Here:

- `name` stores a string value.
- `age` stores an integer value.

Variables allow us to reuse and manipulate data throughout a program.

---

## Data Types

Python supports multiple data types.

### Integer

Stores whole numbers.

```python
count = 10
```

### Float

Stores decimal numbers.

```python
temperature = 25.5
```

### String

Stores text.

```python
project = "Industrial Quality Assurance"
```

### Boolean

Stores logical values.

```python
is_passed = True
```

Understanding data types is important because different operations can be performed on different types of data.

---

## Lists

Lists are ordered collections of items.

Example:

```python
products = ["Bolt", "Nut", "Screw"]
```

Lists can store multiple values in a single variable.

Common operations:

```python
products.append("Washer")
print(products[0])
```

Applications:

- Product inventory
- Defect records
- Sensor readings

---

## Tuples

Tuples are similar to lists but cannot be modified after creation.

Example:

```python
machine_info = ("Machine A", "Running")
```

Tuples are useful when data should remain fixed.

---

## Dictionaries

Dictionaries store data in key-value pairs.

Example:

```python
inspection = {
    "product_id": 101,
    "status": "Pass",
    "defects": 2
}
```

Advantages:

- Structured data storage
- Fast data retrieval
- Easy organization of information

Industrial quality inspection data can often be represented using dictionaries.

---

## Conditional Statements

Conditional statements help programs make decisions.

Example:

```python
defects = 3

if defects > 5:
    print("Fail")
else:
    print("Pass")
```

Applications:

- Product pass/fail decisions
- Quality checks
- Alert generation

---

## Loops

Loops are used to repeat a block of code multiple times.

### For Loop

```python
products = ["Bolt", "Nut", "Screw"]

for product in products:
    print(product)
```

### While Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Benefits:

- Reduces repetitive code
- Efficient processing of large datasets
- Improves automation

---

## Functions

Functions are reusable blocks of code designed to perform specific tasks.

Example:

```python
def square(number):
    return number * number

print(square(5))
```

Benefits:

- Code reusability
- Better organization
- Easier debugging
- Improved readability

Functions are an essential part of software development and machine learning workflows.

---

## Introduction to Machine Learning

As part of Week 1, an introductory overview of Machine Learning was also explored.

Machine Learning is a branch of Artificial Intelligence that enables systems to learn from data and improve performance without being explicitly programmed.

Basic workflow:

1. Collect Data
2. Process Data
3. Train Model
4. Make Predictions

Applications include:

- Defect Detection
- Product Classification
- Predictive Maintenance
- Quality Inspection

---

## Key Learnings

During Week 1, I learned:

- Python syntax and programming basics
- Variables and data types
- Lists, tuples, and dictionaries
- Conditional statements
- Loops
- Functions
- Basic concepts of Machine Learning
