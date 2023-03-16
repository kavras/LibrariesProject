import pandas as pd
import numpy as np

d1 = {
    'Name': ['John', 'Mary', 'Andreas'],
    'Age': [25, 34, 23],
    'Position': ['Data Analyst', 'Project Manager', 'IT']
}

d2 = {
    'Name': ['Elena', 'Kostas', 'George'],
    'Age': [23, 26, 27],
    'Position': ['Operations ass.', 'Data Analyst', 'Sales']
}

df1 = pd.DataFrame(d1, index=[1, 2, 3])    #, index=[1, 2, 3])    for joining
df2 = pd.DataFrame(d2, index=[4, 5, 6])    #, index=[1, 2, 3])
result = pd.concat([df1, df2])
print(result)

result1 = pd.merge(df1, df2, on='Position')
print(result1)

#result2 = df1.join(df2, how='inner')  joining requires different column names between joining dfs
#print(result2)


