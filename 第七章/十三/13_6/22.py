# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 20:16
"""


# ����һ���ಢʹ�ù��캯����ʼ�������ֵ
class Check():
    def __init__(self):
        self.n = []

    # ����������ӡ�ɾ�����������ʾ�б�Ԫ�صķ�����������Ӧ��ֵ
    def add(self, a):
        return self.n.append(a)

    def remove(self, b):
        self.n.remove(b)

    def insert(self, c, d):
        self.n.insert(c, d)

    def dis(self):
        return self.n


# Ϊ�ഴ��һ������
obj = Check()
# ʹ�ö��󣬸����û���ѡ�������Ӧ�ĺ���
choice = 1
while choice != 0:
    print("0. �˳�")
    print("1. ���")
    print("2. ɾ��")
    print("3. ��ʾ")
    print("4. ����")
    choice = int(input("������ѡ��1��2��3��: "))
    if choice == 1:
        n = int(input("��������ӵ�����: "))
        obj.add(n)
        print("������б�Ϊ: ", obj.dis())

    elif choice == 2:
        n = int(input("������ɾ��������: "))
        obj.remove(n)
        print("������б�Ϊ: ", obj.dis())

    elif choice == 3:
        print("�б�Ϊ ", obj.dis())

    elif choice == 4:
        # �ö��ŷָ�����ʽΪ��2,5
        c, d = input('���������λ�ú����֣�').split(',')
        obj.insert(int(c), int(d))
        print("������б�Ϊ: ", obj.dis())

    elif choice == 0:
        print("�˳���!")
    else:
        print("��Чѡ��!!")
