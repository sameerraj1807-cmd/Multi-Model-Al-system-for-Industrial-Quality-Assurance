Cell 1: Introduction
# Week 1 - Python Basics
# Summer of Code Project
# Multi-Modal AI System for Industrial Quality Assurance

print("Hello World!")
print("This is my first Python notebook.")
-------------------------------------------------------------------------------------------------

Cell 2: Variables and Data Types
name = "Sameer Raj"
college = "IIT Bombay"
year = 1

print("Name:", name)
print("College:", college)
print("Year:", year)

print(type(name))
print(type(year))

-------------------------------------------------------------------------------------------------
Cell 3: Numbers
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

-------------------------------------------------------------------------------------------------
Cell 4: Strings
project = "Industrial Quality Assurance"

print(project)

print(project.upper())
print(project.lower())

print("Length:", len(project))

-------------------------------------------------------------------------------------------------
Cell 5: Lists
products = ["Bolt", "Nut", "Screw", "Washer"]

print(products)

print(products[0])
print(products[2])

products.append("Bearing")

print(products)

-------------------------------------------------------------------------------------------------
Cell 6: Tuples
machine = ("Machine_A", "Running")

print(machine)

-------------------------------------------------------------------------------------------------
Cell 7: Dictionary
inspection = {
    "product_id": 101,
    "status": "Passed",
    "defects": 2
}

print(inspection)

print(inspection["status"])

-------------------------------------------------------------------------------------------------
Cell 8: Conditional Statements
defects = 3

if defects > 5:
    print("Product Failed Inspection")
else:
    print("Product Passed Inspection")

-------------------------------------------------------------------------------------------------
Cell 9: For Loop
products = ["Bolt", "Nut", "Screw"]

for product in products:
    print(product)

-------------------------------------------------------------------------------------------------
Cell 10: While Loop
count = 1

while count <= 5:
    print(count)
    count += 1

-------------------------------------------------------------------------------------------------
Cell 11: Mini Example
products = {
    "Bolt": 2,
    "Nut": 1,
    "Screw": 6
}

for item, defects in products.items():

    if defects > 5:
        print(item, "-> Failed Inspection")
    else:
        print(item, "-> Passed Inspection")

