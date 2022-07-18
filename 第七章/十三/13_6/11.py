"""
作者：川川

@时间  : 2022/3/28 3:00
"""


def difference(n):
    if n <= 15:
        return 15 - n
    else:
        return (n - 15) * 2


print(difference(21))
print(difference(14))
