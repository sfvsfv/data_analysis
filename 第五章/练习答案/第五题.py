"""
作者：川川
时间：2023年12月29日
"""
# 第五题
def ou_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum


print(ou_num([4, 5, 9, 2, 3, 7, 8]))