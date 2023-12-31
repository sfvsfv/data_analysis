"""
作者：川川
时间：2023年12月29日
"""

def ch(n):
    return lambda a: a * n


m = ch(3)

print(m(10))