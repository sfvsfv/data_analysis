"""
作者：川川

@时间  : 2022/3/28 3:14
"""
x, y = map(int,input().split())  # 将输入的数字转化为int类型
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))
