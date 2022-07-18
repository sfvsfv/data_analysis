"""
作者：川川

@时间  : 2022/2/27 16:40
"""
a = ["banana", "Orange", "apple", "cherry"]
a.sort()
print(a)

b = ["banana", "Orange", "apple", "cherry"]
b.sort(key=str.lower)
print(b)

c = [1, 5, 6, 8, 4, 2]
c.sort()
print(c)

d = [1, 5, 6, 8, 4, 2]
d.reverse()
print(d)

e = [1, 5, 6, 8, 4, 2]
e.sort()
e.reverse()
print(e)
