"""
作者：川川

@时间  : 2022/3/3 21:08
"""


# class cat:
#     # 属性：品种，毛色
#     # 方法：吃老鼠，猫会爬树
#     def big(self):
#         print('猫会吃老鼠')
#
#     def black(self):
#         print('猫会爬树')


class people(object):
    # 属性：身高，体重
    # 方法：会看书，会吃饭
    def book(self):
        print('人在看书。..')

    def eat(self):
        print('人在吃饭')


# 创建对象
p = people()

p.name = '张三'
p.age = 20
p.sex = '男'

# 调用对象的方法
# p.book()
# p.eat()

print(p.name)
print(p.age)
print(p.sex)

p2 = people()
# 添加属性
p2.name = '李四'
p2.age = 20
p2.sex = '男'
# 获取属性
print(p2.name, p2.age, p2.sex)

