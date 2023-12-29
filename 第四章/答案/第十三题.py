"""
作者：川川
时间：2023年12月29日
"""
name = "mfmefmrrom"
count = 0
for char in name:
    if char != 'm':
        continue
    else:
        count = count + 1

print('m出现的次数为:', count)