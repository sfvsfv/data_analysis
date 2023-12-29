"""
作者：川川
时间：2023年12月29日
"""
num = int(input('i请输入一个整数：'))

m = abs(num)  # 绝对值
if 0 < m < 10:
    print('该数字为一位数')
elif m >= 10 and m < 100:
    print('该数字为两位数')
elif m >= 100 and m < 1000:
    print('该数字为三位数')
else:
    print('该数字至少为四位数')