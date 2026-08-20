import pandas as pd
sales_data = {
    'city': ['Delhi', 'Delhi', 'Noida', 'Noida', 'Delhi'],
    'store': ['Store A', 'Store B', 'Store A', 'Store B', 'Store C'],
    'sales': [25000, 35000, 20000, 30000, 40000]
}

sales_df = pd.DataFrame(sales_data)
city_sales = sales_df.groupby('city')['sales'].sum()
print(city_sales.loc['Noida'])
city_summ = sales_df.groupby('city')['sales'].agg(['mean' , 'count' , 'sum'])
print(city_summ.loc['Delhi'])
city_summary = sales_df.groupby('city')['sales'].sum().reset_index()
print(city_summary)