"""
作者：川川

@时间  : 2022/3/5 23:15
"""


class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class person1(Person):

    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)


x = person1('王', '二')
x.printname()

