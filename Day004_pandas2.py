#Day004: pandas_2
import pandas as pd
"""
Reading data:
    files:
        csv - comma seperated values
        json files
        SQL files from databases
"""
#For csv files - read_csv()
df = pd.read_csv('professors.csv')
df.head() #by default, head gives first 5 datasets
df.head(2) #To get first n datsets provide a numeric digit to head function
df.tail() #by default, tail gives last 5 datasets
df.tail(3) #To get last n datsets provide a numeric digit to tail function
#providing a numeric digit greater than total index will reult in giving entire dataframe

df.info() #info function gives information about entire column

"""
set_index to set index column manually, but indexiong will be from 0 only to 
call or perform indexing and slicing
"""
df.set_index('id', inplace=True)

df['age'].iloc[5]
"""
df['id'] - can't be called after setting it as index
"""

"""
drop() - to delete a row or a column
To drop/delete a column:
df2 = df.drop('salary', axis = 1, inplace=True)
first column name, axis = 1 means entire column, axis = o for row
To drop/delete a row:
df2 = df.drop(3,axis=0, inplace=True)
first index number
"""

#Adding new columns:
df['Annual_salary'] = df['salary']*12

#describe() returns the summary statistics as a dataframe
new = df.describe()
#describe() can be performed on a column too
avg_salary = df['salary'].describe()

#Grouping:
#value_counts() - how many values each column has, also frequency of different values
df['discipline'].value_counts()
#value_counts(normalize=true) - gives different values in percentage
df['discipline'].value_counts(normalize=True)

#For a column with different columns values:
df.groupby('discipline')['salary'].sum()
df.groupby('discipline')['salary'].mean()
df.groupby('discipline')['salary'].min()
df.groupby('discipline')['salary'].max()

#For a column:
df['salary'].sum()
df['salary'].mean()
df['salary'].min()
df['salary'].max()


#Sololearn code challenge:
df1 = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df1.set_index('date', inplace=True)
df1['ratio'] = df1['deaths']/df1['cases']
max_ratio = df1['ratio'].max()
print(df1[df1['ratio'] == max_ratio])
