import numpy as np

prices = np.array([100, 200, 300, 400])

discount = 10

discounted_prices = prices - (prices * discount / 100)

print("Original Prices:", prices)
print("Discounted Prices:", discounted_prices)

data = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print("Column Totals:", np.sum(data, axis=0))
print("Row Totals:", np.sum(data, axis=1))

print("Reshaped Array:")
print(np.reshape(data, (2, 3)))
