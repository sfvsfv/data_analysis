"""
作者：川川
时间：2023年11月1日
"""
a= ('小红','小军','张三')
b = list(a)
b[2]='小川'
c=tuple(b)
print(c)




a= ('小红','小军','张三','李四')
b = list(a)
b[2:4]='小川','小强'
c=tuple(b)
print(c)


a= ('python','how','are','you')
y=list(a)
y.append('hello')
b=tuple(y)
print(b)

a= ('python','how','are','you')
y=list(a)
y.remove('are')
b=tuple(y)
print(b)


