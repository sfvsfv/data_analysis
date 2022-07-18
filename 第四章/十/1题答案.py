"""
作者：川川

@时间  : 2022/3/1 22:05
"""
j = 1
sum = 0
while j < 101:
    if j % 2 == 0:  # 判断偶数
        sum += j
    j += 1
print(sum)
