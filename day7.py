import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme(style="whitegrid")
df = sns.load_dataset('tips')
print(df.head())
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='total_bill', y='tip')
sns.countplot(data=df, x='day',hue='smoker' , palette='pastel')
sns.barplot(data=df, x='day', y='total_bill'  , palette='pastel')
sns.histplot(data=df, x='total_bill', kde=True, color='purple', bins=20)
sns.boxplot(data=df, x='time' , y='total_bill' , palette='pastel')
sns.pairplot(data=df, hue='sex' , palette='husl')

plt.title("Total Bill vs Tip")
plt.show()
plt.title("Number of Customers by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Customer Count")
plt.show()