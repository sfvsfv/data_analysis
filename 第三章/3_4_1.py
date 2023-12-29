"""
作者：川川
时间：2023年12月29日
"""
a = {
    "name": "张三",
    "age": 20,
    "sex": '男'
}
print(type(a))

# 访问字典中单个值
me = {
    "name": "川川",
    "address": "上海",
    "year": 2000
}

x = me["address"]
y = me['year']
z=me.get('name')
print(z)
print(y)
print(x)

print(me.keys())
print(me.values())
print(me.items())


