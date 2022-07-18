# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 12:25
"""


class suan:
    first = 0
    second = 0
    answer = 0

    # 参数化构造函数
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("第一个数字= " + str(self.first))
        print("第二个数字 = " + str(self.second))
        print("两数和 = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# 创建类的对象
# 调用参数化构造函数
obj = suan(100, 50)

# 执行函数
obj.calculate()

# 显示结果
obj.display()
