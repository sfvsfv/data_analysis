# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 13:53
"""


# ����һ���ಢʹ�ù��캯����ʼ�������ֵ
class suan():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


# ȡ�û��ĳ���ֵ
a = int(input("��������ο�: "))
b = int(input("��������γ�e: "))
# Ϊ�ഴ��һ������
obj = suan(a, b)
# ���
print("���Ϊ:", obj.area())
