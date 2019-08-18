import numpy as np
from matplotlib import pyplot as plt

a = np.array([1, 2, 3])

print(a * 3)
print(a + 2)

b = np.array([2, 2, 0])
print(a + b)

print(a / b)

print(a * b)
# 内積
print(np.dot(a, b))

np.arange(10)

# (始点、終点、間隔)
print(np.arange(0, 10, 2))

# 0~10の区間を15等分
print(np.linspace(1, 10, 15))


c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)

# 行列の形状確認
print(c.shape)

d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11,12]],
         [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]])

print(d)

print(d.shape)

print(np.sum(c))

# 軸毎に合計(axis=0 -> 行, axis=1 -> 列)
print(np.sum(c, axis=1))

# 行列の形状を変更
print(c.reshape(3, 2))

print(c.reshape(6, 1))

# 転置
print(c.T)

# 転置
print(np.transpose(c))

# 標準正規分布に従った乱数
print(np.random.randn())

# 0~1までの値の中で乱数
print(np.random.rand())

# インデックス
print("%d : %d : %d" % (a[0], a[1], a[2]))

print("c[0,0]: %d" % c[0, 0])
print("c[0,2]: %d" % c[0, 2])
print("c[1,2]: %d" % c[1, 2])


# スライシング
d = np.array([0, 5, 2, 7, 1, 9])
dd = d[1:5]
print("d[1:5] : %s" % dd)

dd = d[1:3]
print("d[1:3] : %s" % dd)

# [始点:終点:間隔]
dd = d[0:5:2]
print("d[0:5:2] : %s" % dd)

# 配列をひっくり返す
dd = d[::-1]
print("d[::-1] : %s" % dd)

# ブロードキャスティング
# 配列の形状に合わせて適宜配列を拡張してくれる
print("a + c = %s " % (a + c))

print("a * c = %s " % (a * c))


def standard_normal_distribution(x):
    return (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)*1000 # 標準正規分布の確率密度関数を

a = np.random.randn(100000) # 10万個の標準正規分布に従った乱数を生成。
flg = plt.figure()
ax = flg.add_subplot(1,1,1)
x = np.linspace(-5, 5, 1000)
ax.hist(a, bins = 1000)
ax.plot(x, standard_normal_distribution(x))
flg.show()


