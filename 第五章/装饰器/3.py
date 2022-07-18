# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 8:50
"""


def add(x):
    def adder(y):
        return x + y

    return adder


add_sum = add(10)

print(add_sum(10))
