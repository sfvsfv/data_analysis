# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 9:40
"""

import time


# װ��������
def calculate_time(func):
    print('װ������ʼִ��..')

    def inner(*args, **kwargs):
        begin = time.time()
        for j in range(5):
            print(j)
        func(*args, **kwargs)

        end = time.time()
        print("ʱ��һ��Ϊ: ", func.__name__, end - begin)

    return inner


@calculate_time
def jue(num):
    time.sleep(2)
    for i in range(num):
        print(i)


jue(10)
