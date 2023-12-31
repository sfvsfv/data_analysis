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


# x = Person("张", "三")
# x.printname()


class peson1(Person):
    pass
# 子类创建对象
p=peson1('张','三')
p.printname()