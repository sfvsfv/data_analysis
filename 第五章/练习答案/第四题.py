"""
作者：川川
时间：2023年12月29日
"""
# 第四题
def str_res(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1 ]
        index = index - 1
    return rstr1
print(str_res('hello,world'))