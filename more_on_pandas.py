'''
consider the file: "file_name.csv"
table: name         Age  =>lables
      vishal        21   => 0th row
      Mayank        22   => 1th row
      krisp         23   => 2nd row
      
'''
import pandas

data = pandas.read_csv("sile_name.csv")
col_names = data.columns.tolist()

'''
    pandas allows airthmatic operations on each value in columns like:
        new_age = data["Age"]+10 => will return in new_age series.
                                                 0  31
                                                 1  32
                                                 3  33 
'''
new_age = data["Age"] + 10 #see above
'''
also we can do pair-wise operations too,i.e 
mul = dataframe["col1"]*data["col2"]
'''
'''
Normailze the data:
    for normalization we need to calculate maximum in columnn using Series.max() function and then divide column by max term to get range from 0 to 1
'''
max_age = data["Age"].max()
#Normalization:
normalize_age = data["Age"]/max_age
'''
To sort the columns we can use sort_values() method
'''
data.sort_values("Age") # sort the ages and return new dataframe rather than modify                          # previuos one by default but we can do this on previous                           # dataframe also:
'''
The following code sort ages on original dataframe in descending order:
'''
data.sort_values("Age",inplace=True,ascending=False)

'''
Dataframe.pivot_table(index="name", values="Age", aggfunc=numpy.mean):

The first parameter of the method, index tells the method which column to group by. The second parameter values is the column that we want to apply the calculation to, and aggfunc specifies the calculation we want to perform. The default for the aggfunc parameter is actually the mean, so if we're calculating this we can omit this parameter.
'''
'''
 DataFrame.dropna(axis=0 or 1): 0 for rows,1 for columns
 reset_index(drop=True): used to reset index from 0,if drop is not mentioned thn it will create new index and does not drop yhe old one.
'''