import numpy as np

# ベクトル ################################
a = np.array([2, 9, 4])
b = np.array([7, 2, 3])

# ベクトル和 ================================
print("-------- ベクトル和 --------")
print(a + b)

# 内積 ================================
print("-------- ベクトル内積 --------")
c = np.dot(a, b)
print(c)


# list ###################################
l_2d = [[0, 1, 2], [3, 4, 5]]

print(l_2d)
print(type(l_2d))

# 配列 ###################################
print("-------- 配列 --------")
arr = np.array([[4, 3, 2], [1, 2, 3]])
print(arr)
print(type(arr))

arr2 = np.arange(6)
print(arr2)

arr2 = np.arange(6).reshape(2, 3)
print(arr2)

# 行列 Matrix #################################
print("-------- 行列 --------")
mat = np.matrix([[0, 1, 2], [3, 4, 5]])
print(mat)
print(type(mat))

mat = np.matrix(arr)
print(mat)
print(type(mat))

print("-------- 行列和 --------")
ma = np.array([[1, 2], [3, 4]])
mb = np.array([[5, 6], [7, 8]])
mc = ma + mb
print(mc)


print("------------------")
print(ma * mb)
print("-------- 行列積 --------")
print(np.dot(ma, mb))
print(np.dot(mb, ma))


print("-------- 転置行列 --------")
at = np.array([[1, 2, 4], [4, 5, 6]])
print(at.T)

