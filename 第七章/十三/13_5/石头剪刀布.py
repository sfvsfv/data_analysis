# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/8 23:56
"""
import random

choices = ["ʯͷ", "����", "��"]  # ʯͷ������
computer = random.choice(choices)

# player = False
cpu_score = 0
player_score = 0

while True:
    player = input("������ʯͷ/����/����(����qֹͣ)")
    if player == computer:
        print("ƽ��!")
    elif player == "ʯͷ":
        if computer == "��":
            print("������!", "���Ե�",computer, "�ȵù�", player)
            cpu_score += 1
        else:
            print("��Ӯ��!","��ҵ�", player, "�ȵù�", computer)
            player_score += 1
    elif player == "��":
        if computer == "����":
            print("������!", "���Ե�",computer, "�ȵù�", player)
            cpu_score += 1
        else:
            print("��Ӯ��!","��ҵ�", player, "�ȵù�", computer)
            player_score += 1
    elif player == "����":
        if computer == "ʯͷ":
            print("������...", "���Ե�",computer, "�ȵù�", player)
            cpu_score += 1
        else:
            print("��Ӯ��!", "��ҵ�",player, "�ȵù�", computer)
            player_score += 1
    elif player == 'q':
        print("���յ÷�:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        if cpu_score==player_score:
            print('���ս��Ϊƽ��')
        elif cpu_score>player_score:
            print('����Ӯ��Ϊ����')
        else:
            print('����Ӯ��Ϊ�û�')
        break
    else:
        print("����ֵ���ԣ���������ȷֵ")
    computer = random.choice(choices)
