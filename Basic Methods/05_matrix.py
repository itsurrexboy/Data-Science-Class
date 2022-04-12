#05 Take a matrix and do Transpose, take two matrices and do matrix multiplication,
# find sum of k'th and i'th column.
import numpy as np

matrix1 = np.array([[1,2,3],[2,1,3],[3,2,1]])
print('Matrix : \n', matrix1)
#transpose
print('Transpose : \n', np.transpose(matrix1))
#matrix multiplication
matrix2 = np.array([[3,2,1],[2,1,3],[1,2,3]])
print('Matrix 1 :\n', matrix1)
print('Matrix 2 :\n', matrix2)
print('Multiplication of Matrix1 and Matrix2 = \n', matrix1.dot(matrix2))