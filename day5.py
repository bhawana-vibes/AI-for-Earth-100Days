import pandas as pd
import numpy as np
data = {
    'name': ['Amit', 'Sara', 'Rahul', 'Pooja', 'Sara'],
    'age': [25, np.nan, 30, 22, np.nan],      
    'salary': [50000, 45000, np.nan, 52000, 45000],
    'city': ['Delhi', 'Noida', 'Delhi', np.nan, 'Noida']
}

df = pd.DataFrame(data)
print("---original data ---")
print(df)
#print(df.isna().sum())
mean_salary = df['salary'].mean()
#df['salary'] = df['salary'].fillna(mean_salary)
#print(df['salary'])
print(df.duplicated())
df_clean = df.drop_duplicates()

print("--- Duplicates after ---")
print(df_clean)