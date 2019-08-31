import sys
print(sys.stdin.encoding)

value = """The browser displays an 
         error message"""
print(value + ": " + str(len(value)))

# tuple ##############################
print("# tuple ##############################")
a = (2, 5, 8)
b = (8, 3, 7)

print(a)
print(len(a))
print(a * 3)
print(a + b)

# list ##############################
print("# list ##############################")
c = list(a)
print(c)

c.reverse()
print(c)

d = tuple(c)
print(d)

# set ##############################
print("# set ##############################")
aa = set([1, 2, 3, 4])
bb = set([3, 4, 5])

print(aa)
print(bb)

print(aa - bb)
print(aa | bb)
print(aa & bb)
print(aa ^ bb)

# key & value ##############################
ages = {"a": 34, "b": 17, "c": 65}
print("# key & value ##############################")
print(ages)
print(ages["b"])

ages["c"] = 50
print(ages)

ages["d"] = 48
print(ages)

print("a" in ages)
print(ages.keys())
print(ages.values())
print(ages.items())

# for ##############################
print("# for ##############################")
nums = [1, 5, 2, 7]
total = 0

for i in nums:
    print(i)
    total += i
else:
    print(total)

print(sum(nums))

users = {"a": 100, "b": 50, "c": 200}

for key, value in users.items():
    print("key: %s, value: %d" % (key, value))

for key in users.keys():
    print(key)

for value in users.values():
    print(value)

# 関数 ##############################
print("# 関数 ##############################")


def hello(name="john", num=2):
    print("hello, %s! " % name * num)
    return [name, num]


hello()
hello("jack", 3)

funca = hello()
print(funca)

kwargs = {"num": 5, "name": "Paul"}
# 引数辞書
print("# 引数辞書 ##############################")
hello(**kwargs)

# 引数シーケンス
print("# 引数シーケンス(as a tuple) ##############################")


def sample_func(arg1, *arg2):
    print(arg1, arg2)


sample_func('a', 'b', 'c', 'd')


# 引数辞書
print("# 引数辞書(as dictionaries) ##############################")


def sample_fun2(arg1, **arg2):
    print(arg1, arg2)


sample_fun2('a', key1='x', key2='y', key3='z')


# 引数シーケンス & 辞書
print("# 引数シーケンス & 辞書 ##############################")


def sample_fun3(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)


sample_fun3('a', 'b', 'c', 'd', key1='x', key2='y', key3='z')


# map関数 ##############################
print("# map関数 ##############################")


def double(x):
    return x*x*2


print(list(map(double, users.values())))
print(list(map(lambda x: x*x*3, [2, 4, 7])))


def my_func(n: 'この値から足し始める', m: 'この値まで足す') -> 'nからmの合計値':
    """ nからmまでの合計を返す関数 """
    ret = 0
    for i in range(n, m+1):
        ret += i
    return (ret, aa)


print(my_func(2, 6))
