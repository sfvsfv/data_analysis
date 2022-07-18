# coding=gbk
"""
作者：川川
@时间  : 2022/4/10 14:40
"""
year = int(input('请输入年份：'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('{}年为闰年'.format(year))
else:
    print('该年不是闰年')
