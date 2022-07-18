# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 19:59
"""
import math


# 创建一个类并使用构造函数初始化该类的值
class Circle():
    def __init__(self, radius):
        self.radius = radius

    # 创建一个名为 area 的方法，它返回类的面积和一个名为 perimeter 的方法，它返回类的周长
    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# 从用户那里获取radius的值
r = int(input("请输入半径: "))
# 为类创建一个对象
obj = Circle(r)
# 使用对象，调用这两个方法.打印圆的面积和周长
print("面积为:", round(obj.area(), 2))
print("周长为:", round(obj.perimeter(), 2))
