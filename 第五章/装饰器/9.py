# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 10:53
"""


def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)


print(fac(5))
