"""
作者：川川

@时间  : 2022/3/2 19:18
"""


def total(num):
    i = 1
    sum = 0  # 设置初始值为0
    while i < num:
        sum += i
        i += 1
    return sum


# 调用函数
print(total(11))
