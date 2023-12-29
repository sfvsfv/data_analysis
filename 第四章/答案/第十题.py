"""
作者：川川
时间：2023年12月29日
"""
i = 0
res = 1
count = int(input("请告诉我你需要输入几个数字: "))
for i in range(count):
    x = float(input("请输入一个整数: "))
    res =res * x
print("所有数字乘积大小为: ", res)