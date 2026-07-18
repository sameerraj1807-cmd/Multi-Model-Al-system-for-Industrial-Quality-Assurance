import ollama

prompt = """
Generate a professional steel inspection report.

Detected Defects:
- pitted_surface (58.6%)
- pitted_surface (51.7%)
- patches (47.1%)

Include:
1. Summary
2. Severity
3. Recommended Actions
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])