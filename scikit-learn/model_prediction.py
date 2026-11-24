from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
data = load_diabetes()

X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict test data
predictions = model.predict(X_test)

# Evaluate model
print("MODEL PREDICTION")
print("----------------")
print("Mean Absolute Error:",
      mean_absolute_error(y_test, predictions))

# Compare actual and predicted values
print("\nActual vs Predicted:")

for actual, predicted in zip(y_test[:10], predictions[:10]):
    print(f"Actual: {actual:.2f} | Predicted: {predicted:.2f}")

# Predict a new sample
new_sample = X_test[0].reshape(1, -1)

new_prediction = model.predict(new_sample)

print("\nNew Sample Prediction:", new_prediction[0])
