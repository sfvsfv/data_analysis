"""
作者：川川

@时间  : 2022/2/12 15:12
"""
# 一般的输出
# print(789)
# print('今天我要学python', end=" ")
# print('又学会了一点')
# s = 111
# print(s)

print('今天我要学python', end="，我")
print('又学会了一点')

# 格式化输出
name = '小明'
age = 20
price = 2022.5
print('我的姓名是:%s,我的年龄是:%d,我有%f人民币' % (name, age, price))

# 第二种格式化输出
a = 22
b = 4000
c = 4
d = "小明今年 {}岁 ,买了个华为手机, 花费了{}元，他一共攒了 {} 个月"
print(d.format(a, b, c))


c = 22
b = 4000
a = 4
d = "小明今年 {2}岁 ,买了个华为手机, 花费了{1}元，他一共攒了 {0} 个月"
print(d.format(a, b, c))
