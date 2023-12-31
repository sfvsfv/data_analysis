"""
作者：川川
时间：2023年12月29日
"""
# 装饰器函数
def start(fn):
    print("开始..")

    def inner():
        print("一个功能....")
        fn()

    return inner


# 语法糖
@start
def end():
    print("新增加功能")


end()