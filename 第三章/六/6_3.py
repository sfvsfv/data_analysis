"""
作者：川川

@时间  : 2022/2/27 19:55
"""
# 正索引
a = ('hello', 'world', 'python')
print(a[1])
print(a[0])

# 负索引
b = ('hello', 'world', 'python')
print(b[-1])
print(b[-3])

# 范围索引
b = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(b[2:5])

b = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(b[-5:-1])

b = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(b[:5])

# 遍历元组
b = ('hello', 'world', 'python')
for i in b:
    print(i)

b = ('hello', 'world', 'python')
m = 0
while m < len(b):
    print(b[m])
    m = m + 1
