import numpy as np

'''
    creating vector and matrix from lists 
'''
vector = np.array([10,20,30]) # vector[0]=10 , vector[1] = 20 and so on.

#slicing of vector=> vector[0:2]=[10,20] i.e inlude first index(0 here) but not second index(2 here) 

matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]]) # matrix[0,1] = 10 etc.
'''
slicing in case of matrix is quite tricky.think it as matrix[initial_row_index:final_row_index,initial_col_index:final_col_index]

'''

'''
    shape property of numpy returns tuple of dimension of array
'''
vectorShape = vector.shape # o/p=> (3,)  Exp--- 1-D i.e having 1row and 3 columns
matrixShape = matrix.shape # o/p => (3,3)  Exp--- 2-D having 3rows, 3columns

'''
    np.genfromtxt("file.csv",delimiter=",",dtype = "U75",skip_header=1) => To read data from file and returns np.ndarray, skip_header =1 means ignore first row from data. 
    dtype="U75" means we want to read in each value as a 75 byte unicode data type
'''
'''
    dtype => to get data type
'''
vector.dtype # o/p => int64 ---since here vector contains only integers 
'''
    nan => nan is a datatype shows ='Not a number'
'''