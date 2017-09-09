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