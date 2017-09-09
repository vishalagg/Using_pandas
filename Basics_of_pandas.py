import pandas

'''read_csv() : this function of panda is used to read csv file'''
'''
eg. data = pandas.read_csv("file_name")
'''
'''
****To display first n row of table: use head(n), n= no. of rows to be displayed,default is 5
eg: data.head() => returns first 5 rows.
=>  data.head(n) => returns first n rows.
'''

'''
    To access full list of column space,use coloumn attribute
    eg. col_name = data.columns
'''


'''
*********loc[] in pandas: As we use bracket notation in Numpy to access the element, in panda we use loc[] to access, here the advantage is that whenever we want to extract a particular row ,let say 0th row, of a table, the loc[0] method will return 0th row along with labels.
eg:consider the file: "file_name.csv"
table: name         Age  =>lables
      vishal        21   => 0th row
      Mayank        22   => 1th row
      krisp         23   => 2nd row
      
now,first open the file:
    data = pandas.read_csv("file_name.csv")
    zero = data.loc[0] => it will return "series object" ,a data structure:
                          name      Age
                          vishal     21
                          

***we can also pass list or slice in loc[] to access multiple rows but unlike python the slice in loc[] will INLUDE BOTH start and end index.
eg: ls = [0,1]
    zero_and_one = data.loc[ls] =>will return series object:
                                        name      Age
                                        vishal     21
                                        Mayank     22
eg of slice:
    using_slice = data.loc[1:2] =>will return series object:
                                    name          Age
                                    Mayank        22
                                    krisp         23
                                    
                                    *note here both 1st and 2nd rows are inluded
                                    
since loc[] returns series object containing the row label and each row's value for that column. To access a single column, use bracket notation and pass in the column name as a string:
eg:
    age -col = data["Age"] => returns:
                                0   21
                                1   22
                                3   23
                                
To acccess multiple columns we can also pass a list:
eg:       col = data[["Age","name"]] => The order of returned columns will be same as the order of elements we passed in the list.i.e. Age col first then name column.
o/p:            21    vishal
                22    Mayank
                23    krisp
            
                                        
'''

'''
dtype in pandas: pandas have following dtypes(taken from numpy system):

**1. object = to representing string values
2. int = to represent integer value
3. float = "  "       float    "
4. datetime = " "     time    "
5. bool =   "   "     Boolean  "

eg: zero.dtype => will return object i.e string

'''
'''
tolist(): this function is used to convert object into list.
eg:
    col_names = data.columns.tolist()=> returns ['name','Age']
    
    
endswith(): returns columns if endswith given pattern.
eg:
    col_endswith_e = data.endswith('e') => returns=>  name
'''