"""
作者：川川

@时间  : 2022/3/2 22:00
"""


# 第一题
# def avg(a, b, c):
#     return (a + b + c) / 3
# print((avg(6, 3, 6)))


# 第二题
# def Reverse(s):
#     res = s.replace('_', ' ')
#     res2 = res.title()
#     res3 = res2.replace(' ', '')
#     print(res3)
# 调用函数
# Reverse('hello_my_love')
# Reverse('open_door')


# 第三题
# def res(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total
# print(res((4,5,6,-4,3)))

# 第四题
# def str_res(str1):
#
#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[index - 1 ]
#         index = index - 1
#     return rstr1
# print(str_res('hello,world'))


# 第五题
# def ou_num(l):
#     enum = []
#     for n in l:
#         if n % 2 == 0:
#             enum.append(n)
#     return enum
# 
# 
# print(ou_num([4, 5, 9, 2, 3, 7, 8]))


# 第六题
def hui(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(hui('mam')) 
print(hui('hello'))
