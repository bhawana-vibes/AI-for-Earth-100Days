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