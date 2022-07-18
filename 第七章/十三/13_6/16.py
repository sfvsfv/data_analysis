"""
作者：川川

@时间  : 2022/3/28 3:09
"""


def sum(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum


print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))
