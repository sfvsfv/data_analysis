"""
作者：川川
时间：2023年11月1日
"""
a= {'小明','小军','小强'}
a.remove('小明')
print(a)

# 如果不存在该值，不会引发报错
b= {'小明','小军','小强'}
b.discard('小军')
print(b)


c={'hello','python','love'}
c.pop()
print(c)

