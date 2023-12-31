"""
作者：川川
时间：2023年12月29日
"""
def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)


print(fac(5))