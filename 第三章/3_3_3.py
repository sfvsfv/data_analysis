"""
作者：川川
时间：2023年11月1日
"""
set1={'a','b','c'}
set2={1,2,3}
set3=set1.union(set2)
print(set3)


set1.update(set2)
print(set1)


set1={'川川一号','川川二号','川川三号','川川菜鸟'}
set2={'川川一号','川川五号','川川三号','川川菜鸟'}
set1.intersection_update(set2)
print(set1)

set3={'川川一号','川川二号','川川三号','川川菜鸟'}
set4={'川川一号','川川五号','川川三号','川川菜鸟'}
z=set3.intersection(set4)
print(z)