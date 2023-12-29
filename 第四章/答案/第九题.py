"""
作者：川川
时间：2023年12月29日
"""
count = int(input("请告诉我你需要输入几个数字: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("请输入一个整数: "))
    sum = sum + x
avg = sum / count
print("平均值为: ", avg)