Cell 1
# Prompt Engineering Basics

Prompt Engineering refers to designing effective instructions for Large Language Models.

----------------------------------------
Cell 2
## Simple Prompt

----------------------------------------
Cell 3
prompt = """
Explain Machine Learning in simple words.
"""

print(prompt)

----------------------------------------
Cell 4
## Role-Based Prompting

----------------------------------------
Cell 5
prompt = """
You are a quality inspection engineer.

Explain why a scratch on a metal surface can affect product quality.
"""

print(prompt)

----------------------------------------
Cell 6
## Structured Prompting

----------------------------------------
Cell 7
prompt = """
Product Information:

Product ID: 105
Defect: Surface Crack

Generate a short inspection report.
"""

print(prompt)

----------------------------------------
Cell 8
## Few-Shot Prompting

Few-shot prompting provides examples before asking the model to perform a task.

----------------------------------------
Cell 9
prompt = """
Example 1:

Defect: Scratch

Severity: Low

Example 2:

Defect: Crack

Severity: High

Now classify:

Defect: Broken Corner
"""

print(prompt)

----------------------------------------
Cell 10
def inspection_assistant(defect):

    if defect.lower() == "scratch":
        return "Minor surface damage detected."

    elif defect.lower() == "crack":
        return "Major structural defect detected."

    else:
        return "Further inspection required."

print(inspection_assistant("scratch"))
print(inspection_assistant("crack"))
