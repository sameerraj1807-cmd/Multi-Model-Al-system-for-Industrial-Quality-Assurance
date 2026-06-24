Cell 1
# Pandas Practice

----------------------------------------
Learning data handling and analysis using Pandas.
Cell 2
import pandas as pd

----------------------------------------
Cell 3
data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Defects": [2, 5, 1, 7, 3],
    "Inspection_Time": [12, 15, 11, 20, 14]
}

df = pd.DataFrame(data)

df

----------------------------------------
Cell 4
print(df.head())

----------------------------------------
Cell 5
print(df.shape)

----------------------------------------
Cell 6
print(df.columns)

----------------------------------------
Cell 7
print(df["Defects"])

----------------------------------------
Cell 8
average_defects = df["Defects"].mean()

print("Average Defects:", average_defects)

----------------------------------------
Cell 9
max_defects = df["Defects"].max()

print("Maximum Defects:", max_defects)

----------------------------------------
Cell 10
filtered_products = df[df["Defects"] > 3]

filtered_products

----------------------------------------
Cell 11
df["Inspection_Status"] = df["Defects"].apply(
    lambda x: "Fail" if x > 5 else "Pass"
)

df

----------------------------------------
Cell 12
status_count = df["Inspection_Status"].value_counts()

print(status_count)

----------------------------------------
Cell 13
df.describe()

----------------------------------------
Cell 14
total_products = len(df)

failed_products = len(
    df[df["Inspection_Status"] == "Fail"]
)

failure_percentage = (
    failed_products / total_products
) * 100

print("Failure Percentage:", failure_percentage)
