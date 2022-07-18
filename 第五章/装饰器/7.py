# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 10:30
"""


def ji_suan(fn):
    def inner(*args, **kwargs):
        print("这是不定参数长计算...")
        fn(*args, **kwargs)

    return inner


# 使用语法糖装饰函数
@ji_suan
def sum_num(*args, **kwargs):
    result = 0
    for value in args:
        # print(value)
        result += value

    for value in kwargs.values():
        result += value

    print(result)


# 你可以传入任意个的参数，自行尝试
sum_num(4, 5, 6, a=10, b=12)
