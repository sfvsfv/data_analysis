# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 19:59
"""
import math


# ����һ���ಢʹ�ù��캯����ʼ�������ֵ
class Circle():
    def __init__(self, radius):
        self.radius = radius

    # ����һ����Ϊ area �ķ�������������������һ����Ϊ perimeter �ķ���������������ܳ�
    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# ���û������ȡradius��ֵ
r = int(input("������뾶: "))
# Ϊ�ഴ��һ������
obj = Circle(r)
# ʹ�ö��󣬵�������������.��ӡԲ��������ܳ�
print("���Ϊ:", round(obj.area(), 2))
print("�ܳ�Ϊ:", round(obj.perimeter(), 2))
