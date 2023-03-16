import pandas as pd
import numpy as np

####task 1, 1 dimension array####

L = [5, 10, 15, 20, 25]
list1 = pd.Series(L)
print(list1)

####task2, convert 1st column of df as series####

d = {
    'column1': [1, 2, 3, 4, 5, 6],
    'column2': [3, 5, 7, 9, 23, 34],
    'column3': [5, 6, 7, 2, 43, 56]
}

df = pd.DataFrame(d)
c1 = df.iloc[:, 0]
print(c1)
print(type(c1))

####task 3, read file data & print first 20 rows####

df_read = pd.read_csv("data.csv")
print(df_read.head(20))

####task 4, iterate through task 3####

for i,j in df_read.iterrows():
    print(i,j)
