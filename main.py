import numpy as np
import pandas as pd
arr=np.array([1,2,3,4,5])
print(arr)

x=[23,45,34]
my_f_series = pd.Series(x)
print(my_f_series)

####pd.Dataframe function and .loc[:]#####

data = {
    "students": ['Emma','Elena', 'Kostas'],
    "grades": [56,98,93],
    "age": [27,23,26]
}
my_f_df = pd.DataFrame(data)

print(my_f_df.loc[:])

####isnull or notnull function#####

data1={
    "students": ['abc', 'fgr', np.nan, 'lpo'],
    "grades": [10, np.nan, 40, 80]
}
s_df= pd.DataFrame(data1)
print(s_df.isnull())

#####fillna function######

s_df["students"].fillna("no name", inplace=True)
s_df["grades"].fillna("no grade", inplace=True)
print(s_df)

####replace function####

t_df=s_df.replace(to_replace="abc", value="paok")
print(t_df)



