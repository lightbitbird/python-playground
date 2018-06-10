import numpy as np

# 行列 ###################################
l_2d = [[0, 1, 2], [3, 4, 5]]

print(l_2d)
print(type(l_2d))

# 配列 ###################################
arr = np.array([[4, 3, 2], [1, 2, 3]])
print(arr)
print(type(arr))

arr2 = np.arange(6)
print(arr2)

arr2 = np.arange(6).reshape(2, 3)
print(arr2)

# 行列 Matrix #################################
mat = np.matrix([[0, 1, 2], [3, 4, 5]])
print(mat)
print(type(mat))

mat = np.matrix(arr)
print(mat)
print(type(mat))

