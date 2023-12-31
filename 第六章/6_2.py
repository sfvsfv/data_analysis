"""
作者：川川
时间：2023年12月29日
"""

class  people(object):
    def __init__(self, life, home):
        self.life = life
        self.home = home

    # 属性：life呵home
    # 方法：看书,吃饭

    def book(self):
        print('人在看书。。。')

    def eat(self):
        print('人在吃饭.....')

# 创建对象
p3 =people('活的', '中国')


# 调用方法
p3.book()
p3.eat()
# 打印属性值
print('人是%s,家住在%s' % (p3.life,p3.home))

# 属性修改
p3.home='上海'
print('家住在%s'%p3.home)

# 删除对象
p4 = people('活着', '北京')
p5 = people('活着', '成都')
del p4
print('删除对象p4')
