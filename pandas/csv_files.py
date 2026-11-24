import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

students = pd.read_csv("students.csv")

print("CSV Data:")
print(students)

print("\nStudent Names:")
print(students["Name"])
