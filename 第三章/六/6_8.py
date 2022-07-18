"""
作者：川川

@时间  : 2022/2/27 20:42
"""
a = ("苹果", "香蕉", "梨子")
# print(a)
(b, c, d) = a
print(b)
print(c)
print(d)

c = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
(e, f, *g) = c
print(e)
print(f)
print(g)
