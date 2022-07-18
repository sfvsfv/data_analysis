# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 20:16
"""


# 创建一个类并使用构造函数初始化该类的值
class Check():
    def __init__(self):
        self.n = []

    # 创建用于添加、删除，插入和显示列表元素的方法并返回相应的值
    def add(self, a):
        return self.n.append(a)

    def remove(self, b):
        self.n.remove(b)

    def insert(self, c, d):
        self.n.insert(c, d)

    def dis(self):
        return self.n


# 为类创建一个对象
obj = Check()
# 使用对象，根据用户的选择调用相应的函数
choice = 1
while choice != 0:
    print("0. 退出")
    print("1. 添加")
    print("2. 删除")
    print("3. 显示")
    print("4. 插入")
    choice = int(input("请输入选择（1，2，3）: "))
    if choice == 1:
        n = int(input("请输入添加的数字: "))
        obj.add(n)
        print("处理后列表为: ", obj.dis())

    elif choice == 2:
        n = int(input("请输入删除的数字: "))
        obj.remove(n)
        print("处理后列表为: ", obj.dis())

    elif choice == 3:
        print("列表为 ", obj.dis())

    elif choice == 4:
        # 用逗号分割，输入格式为：2,5
        c, d = input('请输入插入位置和数字：').split(',')
        obj.insert(int(c), int(d))
        print("处理后列表为: ", obj.dis())

    elif choice == 0:
        print("退出！!")
    else:
        print("无效选择!!")
