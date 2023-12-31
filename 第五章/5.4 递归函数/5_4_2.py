"""
作者：川川
时间：2023年12月29日
"""


def jie(n):
    if n > 1:
        result = n * jie(n - 1)
    else:
        result = 1
    return result


print(jie(5))
