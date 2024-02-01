'''
Sales (quant * price), Date, Region
'''

import pandas as pd

df = pd.read_csv('daily_sales_data_0.csv')
pink_df = df.copy()

pink_df = pink_df[pink_df['product'] == 'pink morsel']
pink_df['price'] = pink_df['price'].str.replace('$','').astype(float)
pink_df['sales'] = pink_df['price'] * pink_df['quantity']
pink_df = pink_df[['sales', 'date', 'region']]
print(pink_df)
