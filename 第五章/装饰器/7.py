# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 10:30
"""


def ji_suan(fn):
    def inner(*args, **kwargs):
        print("���ǲ�������������...")
        fn(*args, **kwargs)

    return inner


# ʹ���﷨��װ�κ���
@ji_suan
def sum_num(*args, **kwargs):
    result = 0
    for value in args:
        # print(value)
        result += value

    for value in kwargs.values():
        result += value

    print(result)


# ����Դ���������Ĳ��������г���
sum_num(4, 5, 6, a=10, b=12)
