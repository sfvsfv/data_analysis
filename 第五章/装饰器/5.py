# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 9:40
"""

import time


# 装饰器函数
def calculate_time(func):
    print('装饰器开始执行..')

    def inner(*args, **kwargs):
        begin = time.time()
        for j in range(5):
            print(j)
        func(*args, **kwargs)

        end = time.time()
        print("时间一共为: ", func.__name__, end - begin)

    return inner


@calculate_time
def jue(num):
    time.sleep(2)
    for i in range(num):
        print(i)


jue(10)
