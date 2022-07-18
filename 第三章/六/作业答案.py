"""
作者：川川

@时间  : 2022/2/27 21:11
"""
# 第一题
# a = ('小川', '小明', '小红')
# print(a[1])

# 第二题
# b = (1, 2, 3, 5, 6, 9, 8)
# print(len(b))

# 第三题
# c = ('汽车', '轮船', '飞机')
# print(c[-1])

# 第四题
# d = ('汽车', '轮船', '飞机')
# e = list(d)
# e[2] = '坦克'
# f = tuple(e)
# print(f)

# 第五题
# m = (1, 8, 9, 6)
# n = (4, 5, 6)
# z = m + n
# print(z)

# 第六题
# x = 'python'
# y = reversed(x)
# print(tuple(y))

# 第七题

x = (5, 2, 6, 4)
y = (4, 2, 5, 7)
result = tuple(map(sum, zip(x, y)))
print(result)
