# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 10:41
"""


def first(func):
    def inner():
        x = func()
        # ����10*10=100
        return x * x

    return inner


def second(func):
    def inner():
        x = func()
        # ����10
        return 2 * x

    return inner


@first
@second
def num():
    return 5


print(num())

# first(second(num))
