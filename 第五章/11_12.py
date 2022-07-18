"""
作者：川川

@时间  : 2022/3/2 21:11
"""
x = lambda a, b: a + b
print(x(11, 11))

y = lambda a, b: a * b
print(y(5, 6))


def ch(n):
    return lambda a: a * n


m = ch(3)

print(m(10))
