import pandas as pd

data = {
    "Department": ["CS", "IT", "CS", "IT", "CS"],
    "Student": ["Ali", "Ahmed", "Sara", "Usman", "Zara"],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Average Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nDepartment Analysis:")
print(df.groupby("Department")["Marks"].mean())

print("\nTop Students:")
print(df.nlargest(3, "Marks"))
