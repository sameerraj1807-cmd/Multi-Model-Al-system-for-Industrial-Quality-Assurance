Cell 1
# Functions Practice
Cell 2
def greet(name):
    print("Hello", name)

greet("Sameer")
Cell 3
def square(number):
    return number * number

result = square(5)

print(result)
Cell 4
def add(a, b):
    return a + b

print(add(10, 20))
Cell 5
def defect_percentage(defects, total):

    percentage = (defects / total) * 100

    return percentage

print(defect_percentage(5, 100))
Cell 6
def inspection_result(defects):

    if defects > 5:
        return "Fail"

    return "Pass"

print(inspection_result(2))
print(inspection_result(8))
Cell 7
def quality_score(defects):

    score = 100 - defects

    return score

print(quality_score(12))
