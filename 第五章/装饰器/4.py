# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 9:13
"""

# װ��������
def start(fn):
    print("��ʼ..")

    def inner():
        print("һ������....")
        fn()

    return inner


# �﷨��
@start
def end():
    print("�����ӹ���")


end()
