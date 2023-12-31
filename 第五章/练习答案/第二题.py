"""
作者：川川
时间：2023年12月29日
"""
# 第二题
def Reverse(s):
    res = s.replace('_', ' ')
    res2 = res.title()
    res3 = res2.replace(' ', '')
    print(res3)
# 调用函数
Reverse('hello_my_love')
Reverse('open_door')