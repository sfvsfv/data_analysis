"""
作者：川川

@时间  : 2022/2/13 1:34
"""
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# 会报错
# age = 22
# txt =" 川川今年 " + age
# print(txt)

# 修改如下
age = 22
txt = " 川川今年 " + str(age)
print(txt)
