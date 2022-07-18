"""
作者：川川

@时间  : 2022/3/1 21:34
"""
# name = ["小王", '小强', '小明']
# year = [2000, 2001, 2002]
#
# for x in name:
#     for y in year:
#         print(x, y)


for i in range(1, 10):
    for j in range(1, i + 1):
        t = i * j
        print("{0}*{1}={2}".format(i, j, t), end=' ')
    print(" ")
