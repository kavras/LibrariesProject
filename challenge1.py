import pandas as pd
import numpy as np

data = pd.read_csv("1.supermarket.csv")
print(data.head())
print(data.tail())
print('\nShape of dataset: ', data.shape)
print(data.info())

print(data.columns)

df = data.groupby(['item_name'])
df_sum = df.sum()
print(df_sum.head(1))
