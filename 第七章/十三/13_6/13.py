"""
作者：川川

@时间  : 2022/3/28 3:04
"""


def list_count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return count


print(list_count([1, 4, 6, 8, 4]))
print(list_count([1, 4, 6, 4, 7, 4]))
