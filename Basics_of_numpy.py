import numpy as np

'''
    creating vector and matrix from lists 
'''
vector = np.array([10,20,30])

matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

'''
    shape property of numpy returns tuple of dimension of array
'''
vectorShape = vector.shape # o/p=> (3,)  Exp--- 1-D i.e having 1row and 3 columns
matrixShape = matrix.shape # o/p => (3,3)  Exp--- 2-D having 3rows, 3columns

'''
    np.genfromtxt("file.csv",delimiter=",") => To read data from file and returns np.ndarray
'''
'''
    dtype => to get data type
'''
vector.dtype # o/p => int64 ---since here vector contains only integers 
'''
    nan => nan is a datatype shows ='Not a number'
'''