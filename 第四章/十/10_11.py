"""
作者：川川

@时间  : 2022/3/1 22:26
"""
m = 'hello'
match m:
    case "hello":
        print("是hello")
    case "python":
        print("是python")
    case "love":
        print("是love")
    case _:
        print("找不到")

if m == 'hello':
    print("是hello")
elif m == 'python':
    print('是python')
elif m == 'love':
    print('是love')
else:
    print('找不到')
