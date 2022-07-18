# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 13:53
"""


# 创建一个类并使用构造函数初始化该类的值
class suan():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


# 取用户的长宽值
a = int(input("请输入矩形宽: "))
b = int(input("请输入矩形长e: "))
# 为类创建一个对象
obj = suan(a, b)
# 输出
print("面积为:", obj.area())
