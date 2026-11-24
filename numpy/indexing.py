import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("First Three:", numbers[:3])
print("From Second:", numbers[1:])

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("First Row:", matrix[0])
print("Second Column:", matrix[:, 1])
print("Specific Value:", matrix[1, 2])
