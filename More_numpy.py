import numpy as np
'''comparision of array'''
matrix = [[1 2 3],[4 6 7],[90 34 55]]

cmp = matrix[:,1]==6 #o/p=>[False True False]  

x = matrix[cmp,:] #o/p=>[[2 6 34]] i.e select any row in matrix where cmp is True

'''
also     matrix[,:0][matrix[,:0] == 4] =789 => it will replace 4 in 0th col by 789
meaning:  [1 4 90]  [False True False]      => assign 789 where true.      
'''

'''
astype()=> this function is used to convert datatype of an array
eg:lets say we have x = ['7' '9' '8']
then   x = x.astype(float) => 0/p--> [7.0 9.0 8.0]
'''
'''
some function:
sum() -- Computes the sum of all the elements in a vector, or the sum along a dimension in a matrix
mean() -- Computes the average of all the elements in a vector, or the average along a dimension in a matrix
max() -- Identifies the maximum value among all the elements in a vector, or the maximum along a dimension in a matrix

****in case of matrix, we have to indicate the argument-axis=?-> ? will be the dimension on which we are performing any of those function.
eg  matrix.sum(axis=1)
'''