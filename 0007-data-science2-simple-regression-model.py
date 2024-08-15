import numpy as np
from sklearn.linear_model import LinearRegression

import joblib

# too basic:) => model is not the main subject... we're learning Fastapi

# y = a * x + b

np.random.seed(20)

y = np.random.randint(0, 10, 50)

x = np.random.randint(0, 8, 50)

model = LinearRegression()

model.fit(x.reshape(-1,1), y)

print(y)

print(x)

"""
[3 9 4 6 7 2 0 6 8 5 3 0 6 6 0 9 5 7 5 2 6 9 3 3 9 0 6 2 3 1 8 0 2 7 6 6 8
 2 1 3 2 6 9 4 6 4 8 6 2 3]
 
[2 2 1 5 2 1 0 2 2 4 4 3 7 6 4 0 6 0 3 4 0 5 7 5 2 6 1 4 4 7 4 0 4 6 7 6 1
 1 3 6 2 7 1 7 6 1 6 7 0 0]

"""

