"""
作者：川川

@时间  : 2022/2/27 23:21
"""
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
