"""
作者：川川
时间：2023年12月29日
"""
me = {
    "name": "川川",
    "address": "上海",
    "year": 2000
}

# for j in me:
#     print(me[j])
#
#
#
# for i in me.values():
#     print(i)


# for m in me.keys():
#     print(m)



me['tel'] = 123456789
print(me)

for x, y in me.items():
    print(x, y)