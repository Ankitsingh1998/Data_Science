#Day003: pandas_1
"""
pandas - one of most important data science libraries in python.
To read and extract data from files, and perform different operations on it.
"""
import pandas as pd

"""
Pandas is derived from the term "panel data", an econometrics term for data 
sets that include observations over multiple time periods for the same individuals.
series - a column, 1D array
dataframe - multi-dimensional table made up of a collection of series, ndarray
"""

#Dataframes like dictionary(manually created):
#key is like columns, and values are like array
data = {   'ages': [14, 18, 24, 42],
   'heights': [165, 180, 176, 184]
   }

#dataframes in pandas automatically gets numeric index starting from 0
df1 = pd.DataFrame(data)
print(df1)

#But, we can assign different index names to each row
df2 = pd.DataFrame(data, index = ['keyaru','shirley','ronny','lily'])
print(df2)

#loc function to call a row of dataframe
df2.loc['keyaru'] 
df2.loc['lily']

#Indexing:
#To call a column: gives series object
df2['ages']
#To call multiple columns: gives dataframe
df2[['ages','heights']]

#Slicing - iloc function
"""
iloc function similar to slicing in list except for negative indexes it 
will move to right
"""
df2.iloc[2]
df2.iloc[:2]
df2.iloc[1:]
df2.iloc[1:2]
df2.iloc[-2:]
#df2.iloc['shirley':'lily'] - str indexing will not work

#Conditions:
df2[(df2['ages'] > 18) & (df2['heights'] > 170)]
df2[(df2['ages'] > 18) | (df2['heights'] > 170)]
