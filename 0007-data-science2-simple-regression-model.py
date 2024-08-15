import numpy as np
from sklearn.linear_model import LinearRegression

import joblib

# too basic:)

# y = a * x + b

np.random.seed(20)

y = np.random.randint(0, 10, 50)

x = np.random.randint(0, 8, 50)

model = LinearRegression()

model.fit(x.reshape(-1,1), y)

print(y)

print(x)

