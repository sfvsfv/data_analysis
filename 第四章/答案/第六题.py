"""
作者：川川
时间：2023年12月29日
"""
a, b, c = map(int, input('请输入三个数字（空格分开）').split())
if a + b > c and a + c > b and b + c > a:
    print('能组成三角形')
    if a == b or a == c or b == c:
        print('并且还是等腰三角形')
    else:
        print('但是不能组成等腰三角形')
else:
    print('不能组成三角形')