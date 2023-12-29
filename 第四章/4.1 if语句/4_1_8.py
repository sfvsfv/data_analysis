"""
作者：川川
时间：2023年12月29日
"""
ticket = 1  # 1有票 0无票
knife = 5  # 单位cm
if ticket == 1:
    print('有票可以进站了')
    if knife <= 8:
        print('可以上车')
    else:
        print('不允许上车')
else:  # 无票
    print('请先买票再进站')