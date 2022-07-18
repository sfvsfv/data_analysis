# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 12:03
"""


def test():
    # 让x成为全局变量
    global x
    x = "我是字符串"


test()

print("x=" + x)
