import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman"],
    "Age": [22, 24, 21, 23],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

passed = df[df["Marks"] >= 80]

print("Students Who Passed:")
print(passed)

print("\nMarks Above 85:")
print(df[df["Marks"] > 85])

print("\nSorted Students:")
print(df.sort_values("Marks", ascending=False))
