# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 10:41
"""


def first(func):
    def inner():
        x = func()
        # 返回10*10=100
        return x * x

    return inner


def second(func):
    def inner():
        x = func()
        # 返回10
        return 2 * x

    return inner


@first
@second
def num():
    return 5


print(num())

# first(second(num))
