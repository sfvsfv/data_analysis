"""
作者：川川

@时间  : 2022/2/27 17:08
"""
# 第一题
a = ['a', 'b', 'c', 'd', 'e', 'f']
print(a[2])

# 第二题
a = ['a', 'b', 'c', 'd', 'e', 'f']
a[1] = 'm'
print(a)

# 第三题
b = ['z', 'x', 'c']
b.append('b')
print(b)

# 第四题
b = ['z', 'x', 'c']
b.insert(2, 'q')
print(b)

# 第五题
b = ['z', 'x', 'c']
b.remove('x')
print(b)

# 第六题
c = ["小李", "张三", "小明"]
print(c[-2])

# 第七题
d = ['a', 'b', 'c', 'd', 'e', 'f']
print(d[2:6])

# 第八题
e = [5, 6, 2, 8, 9]
e.sort()
e.reverse()
print(e)

# 第九题
a = ['小红', '小明']
b = ['小强', '小张', '小军']
# 直接相加
c = a + b
print(c)
# 使用extend方法
a.extend(b)
print(a)
