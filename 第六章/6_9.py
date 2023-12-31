"""
作者：川川
时间：2023年12月29日
"""
# 声明一个父类A
class a(object):
    def test(self):
        print('父类a')


# 声明一个父类B
class b(object):
    def test(self):
        print('父类b')


# 声明一个子类,同时继承A和B两个父类
class c(a, b):
    pass


# 创建一个对象c
d = c()
d.test()
print(c.__mro__)  # 可以打印查看执行方法的顺序