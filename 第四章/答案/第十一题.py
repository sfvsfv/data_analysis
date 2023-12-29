"""
作者：川川
时间：2023年12月29日
"""
count = 0
sum = 0.0
while (count < 10):
    number = float(input("请输入一个整数: "))
    count = count + 1
    sum = sum + number
avg = sum / 10
print("平均值 :", avg)