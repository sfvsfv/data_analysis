"""
作者：川川

@时间  : 2022/3/5 23:47
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
        self.year = 22

    def info(self):
        print(self.firstname, self.lastname, '年龄为：', self.year)


y = person2('小', '张')
# 获取属性
print(y.year)
# 获取方法
y.info()
