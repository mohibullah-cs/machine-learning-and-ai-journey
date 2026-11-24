import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman"],
    "Age": [22, 24, 21, 23],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("Complete Data:")
print(df)

print("\nFirst Two Rows:")
print(df.head(2))

print("\nInformation:")
print(df.info())

print("\nStatistics:")
print(df.describe())
