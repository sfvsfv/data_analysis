"""
作者：川川

@时间  : 2022/3/28 2:52
"""
a = int(input("请输入n的大小: "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1,n2,n3)
print(n1 + n2 + n3)
