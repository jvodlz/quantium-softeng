import pandas as pd
import os
import re

directory = 'data'
sales_data = []
pattern = re.compile(r'^daily_sales_data_\d+\.csv$')
for filename in os.listdir(directory):
    if pattern.match(filename):
        path = os.path.join(directory, filename)
        sales_data.append(pd.read_csv(path))

sales_combined_df = pd.concat(sales_data)

pink_df = sales_combined_df.copy()
pink_df = pink_df[pink_df['product'] == 'pink morsel']
pink_df['price'] = pink_df['price'].str.replace('$', '').astype(float)
pink_df['sales'] = pink_df['price'] * pink_df['quantity']
pink_df = pink_df[['sales', 'date', 'region']]

pink_df.to_csv('data\pink_morsel_sales.csv', index=False)
