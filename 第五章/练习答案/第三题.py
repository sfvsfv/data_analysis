"""
作者：川川
时间：2023年12月29日
"""
# 第三题
def res(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(res((4,5,6,-4,3)))
