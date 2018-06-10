from numpy.polynomial.polynomial import Polynomial
import math
import sympyExercise

# 2次方程式 ####################################
f = Polynomial([24, -10, 1])
print(f.roots())

# 連立方程式 ####################################
from numpy.linalg import solve
left = [[1, 1, 1], [1, 3, 4], [2, 2, 1]]
right = [3, 13, 4]

print(solve(left, right))


# 順列 組み合わせ ####################################
from itertools import permutations, combinations

balls = [1, 2, 3]
print(list(permutations(balls, 2))) #順列
print(list(combinations(balls, 2))) #組み合わせ

# 集合 ####################################
a = set([1, 2, 3, 4, 5])
b = set([1, 4])
print(a >= b)
print(a | b)
print(a & b)


# 虚数・複素数 ####################################
print(10j * 10j)

print(1j + 1)
print(2j * 2)
print(2j / 1j + 2j)

aj = 2*3j + 2j*3j
print(aj)
print(aj.real)
print(aj.imag)

# 最大公約数, 最小公倍数 ####################################
six = 6
four = 4
# 最大公約数
print(math.gcd(six, four))

# 最小公倍数
# /を使うと結果が小数floatになるため、小数点以下を切り捨て整数の除算結果を返す//（整数除算）を使っている。
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm(six, four))


