import pandas as pd
import numpy as np

df=pd.read_csv("finance_liquor_sales.csv")
print(df.head())
print(df.tail())
print(df.info())

#mean, median, min, max same#
mean = df.mean(numeric_only=True)
print(mean)

median = df.median(numeric_only=True)
print(median)

summary = df.describe()
print(summary)

group = df.groupby('category_name')
print(group.aggregate(np.sum))

###1st group by cn and c and then aggregate based on bottles sold with sum and sale dollars with mean####
grbycc = df.groupby(['category_name', 'city'])
print(grbycc.agg({'bottles_sold': 'sum', 'sale_dollars': 'mean'}))

#### group by vendor name #####
ng = df.groupby('vendor_name')
print(ng.filter(lambda x: len(x)>=20))