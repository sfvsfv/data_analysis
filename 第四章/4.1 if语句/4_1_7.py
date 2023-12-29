"""
作者：川川
时间：2023年12月29日
"""
# password = 123456
# finger = 1  # 假设1代表指纹正确 ，0表示不正确

p = int(input('请输入支付密码：'))
f = int(input('请输入指纹（0/1）：'))

if p == 123456 or f == 1:
    print('支付成功')
else:
    print('支付失败')