'''
consider the file: "file_name.csv"
table: name         Age  =>lables
      vishal        21   => 0th row
      Mayank        22   => 1th row
      krisp         23   => 2nd row
      
'''
import pandas as pd

data = pd.read_csv("sile_name.csv")
col_names = data.columns.tolist()

'''
In python null value is indicated by: None
In pandas null value is indicated by = NaN

we can check for NaN values in columns using pandas.isnull() function which returns list of True or False
'''
age = data["Age"]
Age_is_null = pd.isnull("age") #=> [False False False]

'''
if want to calculate mean of the column which contains NaN also, we have to first extract which do not contains NaN then only we can calculate its correct mean:
'''
good_ages = data['Age'][Age_is_null==False]
mean = sum(good_ages)/len(good_ages)
'''
**But pandas takes care of it and provides mean() function which takes care of NaN
'''
mean = data['Age'].mean()

'''
Series.uinque() or df['col'].unique() => returns unique elements.
'''

'''
************************
Series.value_counts() => let say a column has values either yes or no or cantsay etc. then value_counts() will count all yes,no and cantsay etc. and returns them.
'''