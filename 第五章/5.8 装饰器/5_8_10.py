"""
作者：川川
时间：2023年12月29日
"""
memory = {5: 120, 6: 720}


def ji_yi(f):
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


@ji_yi
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(facto(6))