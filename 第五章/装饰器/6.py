# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 10:16
"""


# ��������־�Ĺ���
def ji_suan(fn):
    def add(num1, num2):
        print('��ʼ����...')
        jian = num1 - num2
        print(jian)
        res = fn(num1, num2)

        return res

    return add


# ʹ���﷨������װ����װ�κ���
@ji_suan
def sum_num(a, b):
    res = a + b
    return res


result = sum_num(5, 6)
print(result)
