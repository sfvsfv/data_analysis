"""
作者：川川

@时间  : 2022/3/5 22:39
"""


class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


# x = Person("张", "三")
# x.printname()


class person1(Person):
    pass


p = person1('张', '三')
p.printname()
