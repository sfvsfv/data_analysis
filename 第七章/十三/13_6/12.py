"""
作者：川川

@时间  : 2022/3/28 3:01
"""


def he(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(he(3, 4, 3))
print(he(3, 3, 3))
