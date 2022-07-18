"""
作者：川川

@时间  : 2022/3/28 3:11
"""


def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum


print(sum(11, 6))
print(sum(19, 6))
