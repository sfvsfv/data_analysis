"""
作者：川川
时间：2023年12月29日
"""

# 单独提一下全局变量

def chuan():
    global x
    x = 2024
    print(x)
chuan()


def han():
    print(x)

han()