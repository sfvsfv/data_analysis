"""
作者：川川

@时间  : 2022/3/1 18:59
"""
u = '川川'
q = 123456

user = input('请输入用户名：')
password = int(input('请输入密码:'))

if user == '川川' and password == 123456:
    print('恭喜，可以进入')
else:
    print('你的用户名或者密码错误')
