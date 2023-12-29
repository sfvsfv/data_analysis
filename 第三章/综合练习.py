"""
作者：川川
时间：2023年12月29日
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



# 第10题
# a = ('小川', '小明', '小红')
# print(a[1])

# 第11题
# b = (1, 2, 3, 5, 6, 9, 8)
# print(len(b))

# 第12题
# c = ('汽车', '轮船', '飞机')
# print(c[-1])

# 第13题
# d = ('汽车', '轮船', '飞机')
# e = list(d)
# e[2] = '坦克'
# f = tuple(e)
# print(f)

# 第14题
# m = (1, 8, 9, 6)
# n = (4, 5, 6)
# z = m + n
# print(z)

# 第15题
# x = 'python'
# y = reversed(x)
# print(tuple(y))

# 第16题
# x = (5, 2, 6, 4)
# y = (4, 2, 5, 7)
# result = tuple(map(sum, zip(x, y)))
# print(result)



# 第17题
# set1 = {"张三", "小王", "小强"}
# print('小强' in set1)
#
# if '小强' in set1:
#     print('存在')

# 第18题
# set2 = {"张三", "小王", "小强"}
# set2.pop()
# set2.remove('小强')
# set2.discard('小强')
# print(set2)

# 第19题
# set3 = {'hello', 'python', 'my'}
# set4 = {'hello', 'set'}
# set3.intersection_update(set4)
# print(set3)

# 第20题
# set5 = {4, 2, 6, 7, 9, 14, 1}
# print(max(set5))
# print(min(set5))

# 第21题
# user_input = input('请输入一段字符：')
# set6 = {'hello', 'python', 4, 5, 2}
# print(user_input in set6)


# 第22题
# sn1 = {1, 2, 3, 4, 5}
# sn2 = {4, 5, 6, 7, 8}
# sn1.difference_update(sn2)
# sn1 -= sn2
# print(sn1)


# 第23题
stu = {
    'id': 1569,
    'name': '小王',
    'sex': '男'
}
print(stu)

print(stu['name'])

stu['name'] = '小明'
print(stu)


for x, y in stu.items():
    print(x, y)

# 第24题
stu2 = {
    "user1": {
        'id': 1569,
        'name': '小王',
        'sex': '男'
    },
    'user2': {
        'id': 7456,
        'name': '小红',
        'sex': '女'
    }
}
print(stu2)

# 第25题
print(stu2['user2']['id'])

