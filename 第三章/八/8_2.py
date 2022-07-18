"""
作者：川川

@时间  : 2022/2/28 10:17
"""
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
