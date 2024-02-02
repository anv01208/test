import pandas as pd

sales_2021 = pd.read_csv('sales_2021.csv')
sales_2022 = pd.read_csv('sales_2022.csv')

merged_sales = pd.merge(sales_2021, sales_2022, on='product_id', suffixes=('_2021', '_2022'))

merged_sales['total_revenue'] = merged_sales['revenue_2021'] + merged_sales['revenue_2022']

result_df = merged_sales[['product_id', 'total_revenue']]

result_df.to_csv('result.csv', index=False)
