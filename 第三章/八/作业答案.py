"""
作者：川川

@时间  : 2022/3/1 14:17
"""
# 第一题
stu = {
    'id': 1569,
    'name': '小王',
    'sex': '男'
}
print(stu)
# 第二题
print(stu['name'])

# 第三题
stu['name'] = '小明'
print(stu)

# 第四题
for x, y in stu.items():
    print(x, y)

# 第五题
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

# 第六题
print(stu2['user2']['id'])
