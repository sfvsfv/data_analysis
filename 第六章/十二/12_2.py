# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 12:25
"""


class suan:
    first = 0
    second = 0
    answer = 0

    # ���������캯��
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("��һ������= " + str(self.first))
        print("�ڶ������� = " + str(self.second))
        print("������ = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# ������Ķ���
# ���ò��������캯��
obj = suan(100, 50)

# ִ�к���
obj.calculate()

# ��ʾ���
obj.display()
