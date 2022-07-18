# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 0:14
"""
# 第三题
# count = int(input("请告诉我你需要输入几个数字: "))
# i = 0
# sum = 0
# for i in range(count):
#     x = int(input("请输入一个整数: "))
#     sum = sum + x
# avg = sum / count
# print("平均值为: ", avg)


# 第四题
# i = 0
# res = 1
# count = int(input("请告诉我你需要输入几个数字: "))
# for i in range(count):
#     x = float(input("请输入一个整数: "))
#     res =res * x
# print("所有数字乘积大小为: ", res)


# 第五题
count = 0
sum = 0.0
while (count < 10):
    number = float(input("请输入一个整数: "))
    count = count + 1
    sum = sum + number
avg = sum / 10
print("平均值 :", avg)
