import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

print(x)
print(y)

model = LinearRegression()
model.fit(x, y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print("CoEfficient of determination ", r_sq)

new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
print("Intercept ",new_model.intercept_)
print("Slope", new_model.coef_)

# Predict
y_pred = model.predict(x)
print("Predicted response", y_pred, sep='\n')

# Predict the response
y_pred = model.intercept_ + model.coef_ * x
print("Predicted response ", y_pred, sep='\n')

# Creating the arrangement with x actor
print("Creating the arrangement")
x_new = np.arange(5).reshape((-1, 1))
print(x_new)

# Model predict with Y actor
print("Model Predict")
y_new = model.predict(x_new)
print(y_new)


