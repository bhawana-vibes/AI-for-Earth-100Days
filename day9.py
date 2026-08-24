import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

df = pd.DataFrame({'Age': [20, 30, 40], 'Salary': [20000, 50000, 80000]})

min_max = MinMaxScaler()
df_scaled = pd.DataFrame(min_max.fit_transform(df), columns=df.columns)
print("Scaled Data (0 to 1):\n", df_scaled)
features = np.array([2, 3])
weights = np.array([4, 5])
print("\nPrediction (Dot Product):", np.dot(features, weights))


flat_features = np.array([3, 2, 1])  
rates = np.array([10, 5, 2])         

predicted_price = np.dot(flat_features, rates)

print("Flat ki Predicted Price (Lakh me):", predicted_price)

import numpy as np
X = np.array([
    [3, 2, 1],
    [2, 1, 2]
])

W = np.array([10, 5, 2])

b = 3

predictions = np.dot(X, W) + b

print("--- House Price Prediction (Y = WX + b) ---")
print("Flat 1 Price (Lakh me):", predictions[0])
print("Flat 2 Price (Lakh me):", predictions[1])