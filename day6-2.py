import matplotlib.pyplot as plt
import pandas as pd
#sales_data = {
    #'city': ['Delhi', 'Delhi', 'Noida', 'Noida', 'Delhi'],
    #'store': ['Store A', 'Store B', 'Store A', 'Store B', 'Store C'],
    #'sales': [25000, 35000, 20000, 30000, 40000]
#}

#sales_df = pd.DataFrame(sales_data)
#city_sales = sales_df.groupby('city')['sales'].sum()
#city_sales.plot(kind='bar', color=['orange', 'teal'])
#plt.title("Total Sales by City")
#plt.xlabel("City")
#plt.ylabel("Total Sales (INR)")
#plt.xticks(rotation=0)
#plt.show()


#df = pd.DataFrame({'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 'profit': [12000, 18000, 15000, 22000, 28000, 35000]})

#df.plot(x='month', y='profit', marker='o', grid=True)
#plt.show()

#df = pd.DataFrame({'salary': [25, 28, 30, 32, 35, 36, 75, 80, 85, 90]})

#df['salary'].plot(kind='hist', bins=10 , edgecolor='black')
#plt.show()



#df = pd.DataFrame({
  #  'experience_years': [1, 2, 3, 4, 5, 6, 7],
 #   'salary_in_lakhs':  [4, 5, 7, 9, 12, 16, 20]
#})

#df.plot(kind='scatter', x='experience_years', y='salary_in_lakhs', color='red')
#plt.show()


df = pd.DataFrame({
    'experience_years': [1, 2, 3, 4, 5, 6],
    'salary_in_lakhs':  [12, 10, 8, 6, 4, 2]
})

df.plot(kind='scatter', x='experience_years', y='salary_in_lakhs', marker='v' , s=100 , color='blue')
plt.show()


