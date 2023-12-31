# coding=gbk
"""
作者：川川
@时间  : 2023/12/8 23:07
"""
from MyQR import myqr

# 动态二维码
myqr.run(
  words='https://hi.zhangsan.cloud/chat',
  picture='1.gif',
  colorized=True,
  save_name='test.gif'
)