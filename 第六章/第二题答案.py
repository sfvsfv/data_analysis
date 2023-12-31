"""
作者：川川
时间：2023年12月29日
"""
class area():
    # 创建一个类并使用构造函数初始化该类的值
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 创建两个数字的加减乘除方法并返回各自的结果
    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


# 将这两个数字作为输入，并为类创建一个对象，将这两个数字作为参数传递给该类
a = int(input("请输入第一个数字: "))
b = int(input("请输入第二个数字: "))
obj = area(a, b)
choice = 1

while choice != 0:
    print("0. 退出")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 出发")
    # 使用对象，根据用户的选择调用相应的函数
    choice = int(input("输入你的选择: "))
    if choice == 1:
        print("Result= ", obj.add())
    elif choice == 2:
        print("Result=", obj.sub())
    elif choice == 3:
        print("Result=", obj.mul())
    elif choice == 4:
        print("Result= ", round(obj.div(), 2))
    elif choice == 0:
        print("退出!")
    else:
        print("输入无效!!")
