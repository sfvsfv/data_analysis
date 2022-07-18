"""
作者：川川

@时间  : 2022/2/28 11:19
"""
me = {
    "name": "川川",
    "address": "上海",
    "year": 2000
}

# for i in me.values():
#     print(i)
#
# for m in me.keys():
#     print(m)

me['tel'] = 123456789
print(me)

for x, y in me.items():
    print(x, y)
