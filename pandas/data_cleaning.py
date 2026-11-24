import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", None, "Sara"],
    "Age": [22, None, 23, 21],
    "Marks": [85, 90, None, 78]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(0)

print("\nCleaned Data:")
print(df)
