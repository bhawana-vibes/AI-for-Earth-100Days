import pandas as pd
import matplotlib.pyplot as plt
raw_data = {
    'employee_id': [101, 102, 103, 104, 105, 105],  
    'department': ['IT', 'HR', 'IT', 'Sales', 'Sales', 'Sales'],
    'salary': [60000, None, 75000, 50000, 55000, 55000] 
}

df = pd.DataFrame(raw_data)
df = df.drop_duplicates()                     
df['salary'] = df['salary'].fillna(45000)  
dept_salary = df.groupby('department')['salary'].sum()
dept_salary.plot(kind='bar', color='teal', edgecolor='black')
plt.title("Total Salary Expenditure by Department")
plt.xlabel("Department")
plt.ylabel("Total Salary (INR)")
plt.xticks(rotation=0)
plt.show()  