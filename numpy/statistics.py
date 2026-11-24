import numpy as np

marks = np.array([75, 80, 65, 90, 85, 70])

print("Marks:", marks)
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

print("Sorted Marks:", np.sort(marks))
