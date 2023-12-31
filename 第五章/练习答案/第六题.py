"""
作者：川川
时间：2023年12月29日
"""
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