# coding=gbk
"""
作者：川川
@时间  : 2022/3/8 23:56
"""
import random

choices = ["石头", "剪刀", "布"]  # 石头剪刀布
computer = random.choice(choices)

# player = False
cpu_score = 0
player_score = 0

while True:
    player = input("请输入石头/剪刀/布：(输入q停止)")
    if player == computer:
        print("平局!")
    elif player == "石头":
        if computer == "布":
            print("你输了!", "电脑的",computer, "比得过", player)
            cpu_score += 1
        else:
            print("你赢了!","玩家的", player, "比得过", computer)
            player_score += 1
    elif player == "布":
        if computer == "剪刀":
            print("你输了!", "电脑的",computer, "比得过", player)
            cpu_score += 1
        else:
            print("你赢了!","玩家的", player, "比得过", computer)
            player_score += 1
    elif player == "剪刀":
        if computer == "石头":
            print("你输了...", "电脑的",computer, "比得过", player)
            cpu_score += 1
        else:
            print("你赢了!", "玩家的",player, "比得过", computer)
            player_score += 1
    elif player == 'q':
        print("最终得分:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        if cpu_score==player_score:
            print('最终结果为平局')
        elif cpu_score>player_score:
            print('最终赢家为电脑')
        else:
            print('最终赢家为用户')
        break
    else:
        print("输入值不对，请输入正确值")
    computer = random.choice(choices)
