# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 1:25
"""
import pyautogui

# moveRel������������λ�������ƶ�280���������ƶ�50
pyautogui.moveRel(280, 50, duration=1)

# ������
pyautogui.click()

# ������ƶ���
pyautogui.moveTo(1000, 635, duration=1)


# # Ĭ��Ϊ�������Ӳ���Ϊ�һ�
# pyautogui.click(button="right")
#
# # �ƶ���ָ��λ��
# pyautogui.moveTo(1200, 621, duration=1)
#
# # ���
# pyautogui.click()
