"""
作者：川川

@时间  : 2022/3/28 2:57
"""
from datetime import date
f_date = date(2022, 3, 2)
l_date = date(2022, 4, 11)
delta = l_date - f_date
print(delta.days)
