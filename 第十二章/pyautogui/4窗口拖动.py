# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 1:34
"""
import pyautogui

# �ƶ���Ŀ��λ��
pyautogui.moveTo(356, 1060, duration=1)

# ������
pyautogui.click()

# �ƶ���Ŀ��λ��
pyautogui.moveTo(1077, 192, duration=1)

# ��ק��λ�ã�500��500��
pyautogui.dragTo(500, 500, duration=1)

# �������λ�����������ƶ�50
pyautogui.dragRel(50, 50, duration=1)
