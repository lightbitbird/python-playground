import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)
print(sys.stderr.encoding)

value = """The browser displays an 
         error message"""
print(value + ": " + str(len(value)))

# tuple ##############################
a = (2, 5, 8)
b = (8, 3, 7)

print(a)
print(len(a))
print(a * 3)
print(a + b)

# list ##############################
c = list(a)
print(c)

c.reverse()
print(c)

d = tuple(c)
print(d)


# set ##############################
aa = set([1, 2, 3, 4])
bb = set([3, 4, 5])

print(aa)
print(bb)

print(aa - bb)
print(aa | bb)
print(aa & bb)
print(aa ^ bb)

# key & value ##############################
ages = {"a":34, "b":17, "c":65}
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
nums = [1, 5, 2, 7]
total = 0

for i in nums:
    print(i)
    total += i
else:
    print(total)

print(sum(nums))


users = {"a":100, "b":50, "c":200}

for key, value in users.items():
    print("key: %s, value: %d" % (key, value))

for key in users.keys():
    print(key)

for value in users.values():
    print(value)

# 関数 ##############################
def hello(name="john", num = 2):
    print("hello, %s! " % name * num)
    return [name, num]

hello()
hello("jack", 3)

funca = hello()
print(funca)

kwargs = {"num": 5, "name": "Paul"}
hello(**kwargs)

# map ##############################
def double(x):
    return x*x*2

print(list(map(double, users.values())))
print(list(map(lambda x: x*x*3, [2, 4, 7])))
