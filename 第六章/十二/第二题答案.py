# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 13:36
"""


class area():
    # ����һ���ಢʹ�ù��캯����ʼ�������ֵ
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # �����������ֵļӼ��˳����������ظ��ԵĽ��
    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


# ��������������Ϊ���룬��Ϊ�ഴ��һ�����󣬽�������������Ϊ�������ݸ�����
a = int(input("�������һ������: "))
b = int(input("������ڶ�������: "))
obj = area(a, b)
choice = 1

while choice != 0:
    print("0. �˳�")
    print("1. �ӷ�")
    print("2. ����")
    print("3. �˷�")
    print("4. ����")
    # ʹ�ö��󣬸����û���ѡ�������Ӧ�ĺ���
    choice = int(input("�������ѡ��: "))
    if choice == 1:
        print("Result= ", obj.add())
    elif choice == 2:
        print("Result=", obj.sub())
    elif choice == 3:
        print("Result=", obj.mul())
    elif choice == 4:
        print("Result= ", round(obj.div(), 2))
    elif choice == 0:
        print("�˳�!")
    else:
        print("������Ч!!")

