"""
作者：川川

@时间  : 2022/3/28 3:06
"""


def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd


print("12和17最大公约数 ：", gcd(12, 17))
print("4和最大公约数：", gcd(4, 6))
print("336和360最大公约数 ：", gcd(336, 360))
