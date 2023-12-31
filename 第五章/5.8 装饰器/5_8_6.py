"""
作者：川川
时间：2023年12月29日
"""
# 添加输出日志的功能
def ji_suan(fn):
    def add(num1, num2):
        print('开始计算...')
        jian = num1 - num2
        print(jian)
        res = fn(num1, num2)

        return res

    return add


# 使用语法他并非装饰器装饰函数
@ji_suan
def sum_num(a, b):
    res = a + b
    return res


result = sum_num(5, 6)
print(result)