"""
作者：川川

@时间  : 2022/3/5 23:40
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


y = person2('小', '明')
# 获取方法
y.printname()
