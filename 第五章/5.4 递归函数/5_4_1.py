"""
作者：川川
时间：2023年12月29日
"""
def jie(n):
    result =1
    for i in range(1,n+1):
        result *= i
    return  result

print(jie(5))