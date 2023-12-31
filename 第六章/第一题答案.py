"""
作者：川川
时间：2023年12月29日
"""
class person(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return str(self.name)

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age


m = person('张三', '男', 22)
print(m.get_name())
print(m.get_age())
print(m.get_sex())