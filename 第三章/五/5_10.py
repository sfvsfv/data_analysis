"""
作者：川川

@时间  : 2022/2/27 17:00
"""
a = ['a', 'b', 'c', 'd', 'e', 'f']
b = ['z', 'x', 'c']
c = a + b
print(c)

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = ['z', 'x', 'c']
a.extend(b)
print(a)