"""
作者：川川
时间：2023年12月29日
"""
me = {
    "name": "川川",
    "address": "上海",
    "year": 2000
}

me['name'] = '张三'
print(me)

me.update({'name': '小王'})
print(me)





me = {
    "name": "川川",
    "address": "上海",
    "year": 2000
}
me['age']=20
print(me)




me = {
    "name": "川川",
    "address": "上海",
    "year": 2000
}
me.pop('name')
print(me)
