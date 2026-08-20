import matplotlib.pyplot as plt
import pandas as pd
sales_data = {
    'city': ['Delhi', 'Delhi', 'Noida', 'Noida', 'Delhi'],
    'store': ['Store A', 'Store B', 'Store A', 'Store B', 'Store C'],
    'sales': [25000, 35000, 20000, 30000, 40000]
}

sales_df = pd.DataFrame(sales_data)
city_sales = sales_df.groupby('city')['sales'].sum()
city_sales.plot(kind='bar', color=['orange', 'teal'])
plt.title("Total Sales by City")
plt.show()