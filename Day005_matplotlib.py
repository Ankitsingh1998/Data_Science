#Day005: matplotlib
"""
graphs
charts
different figures
customization - changing colors, labels, etc
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('professors.csv')

df.columns
df['salary'].plot(kind='bar')

"""
To save the figure
plt.savefig('plot.png')
"""
#By default, x-axis gets assigned with index unless we provide new index to be displayed on x-axis
#line plot: only plot() will give a line plot
df1 = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df1['date'] = pd.to_datetime(df1['date'], format="%d.%m.%y")
df1['month'] = df1['date'].dt.month
#For single plot:
df1[df1['month']==6]['cases'].plot()
#For multiple plot:
df1[df1['month']==6][['cases','deaths']].plot()

#bar plot: kind argument inside plot() function
df = pd.read_csv('professors.csv')
#For single plot:
df['salary'].plot(kind='bar') #bar for vertical graph
df['salary'].plot(kind='barh') #barh for horizontal graph
#For multiple plot:
df['annual_salary'] = df['salary']*12
df[['salary','annual_salary']].plot(kind='bar', stacked=True) #stacked result
df[['salary','annual_salary']].plot(kind='bar', stacked=False) #seperate bars
#stacked tells whether to stack both bars, For true --> Yes, For False --> No
df.set_index('firstname', inplace=True) #Index changed to place it at x-aixs
df[['salary','annual_salary']].plot(kind='bar') #seperate bars

#Box plot:
"""
Box plot: used to visualize the distribution of values ina column, 
basically visualizing the result of the describe() function
"""
df['annual_salary'].plot(kind='box')
"""
green line - median value
box shows the upper and lower quartiles(25% of the data is greater or less 
than these values)
circle shows the outliers
black lines shows the min and max values excluding the outliers
"""

#Histogram:
"""
Similar to box plots, histograms shows distribution of data.
Visually they are similar to bar charts.
They shows frequency for a group of data rather than an individual data point;
hence containing no spaces between them.
It groups data into chunks or bins.
"""
df['annual_salary'].plot(kind='hist')
#chunks can be decided on our own by using bins argument in plot() function
df['annual_salary'].plot(kind='hist', bins=5)

#Area plot: 
df[['salary','annual_salary']].plot(kind='area') #By default stacked=True
df[['salary','annual_salary']].plot(kind='area',stacked=True)
df[['salary','annual_salary']].plot(kind='area',stacked=False)

#Scatter plot: to show relationship between two variables
#requires x and y labels as column names to plot the graph
df[['salary','annual_salary']].plot(kind='scatter', x='salary',y='annual_salary')
df[['salary','annual_salary']].plot(kind='scatter', x='annual_salary',y='salary')

#Pie plot: to show percentage or proportional data
#usually used when we have upto 6 categories
df['salary'].plot(kind='pie')
df['annual_salary'].plot(kind='pie')    
  
#Plot formatting:
#legend argument - specifies whether or not to show the legend
#xlabel to change x-axis
#ylabel to change y-axis
#By default, pandas selects index as x-label as seen in above examples
#pandas leaves y-label empty unless assigned
#suptitle() function - to set the title of a graph
#line plot: without showing legend
df[['salary','annual_salary']].plot(kind = 'line', legend=False)
plt.xlabel('employee name')
plt.ylabel('salary in lacs')
plt.suptitle('Salary vs annual income of employees')  
df.set_index('firstname', inplace=True)   

#bar plot: color changing
df[['salary','annual_salary']].plot(kind = 'bar', legend=True, stacked=False, color=['#1970E7', '#E73E19'])
plt.xlabel('employee name')
plt.ylabel('salary in lacs')    
plt.suptitle('Salary vs annual income of employees')
df.set_index('firstname', inplace=True) 

