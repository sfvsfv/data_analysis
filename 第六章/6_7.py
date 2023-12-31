"""
作者：川川
时间：2023年12月29日
"""
class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class person2(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.year = 2022


y = person2('小', '张')
# 获取属性
print(y.year)
# 获取方法
y.printname()