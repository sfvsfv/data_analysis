# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 23:01
"""
import pyautogui
import time
import pyperclip
pyautogui.moveTo(394, 1068, duration=0.5)

pyautogui.click(clicks=1,button='left')

li=['��֪��������ر𣬺ͱ��Ů����һ��','������ɢ���������� ����������','����·�����ͨ�������������Ϻ���ζ��']
for i in range(3):
    for j in li:
        pyperclip.copy(j)
        pyautogui.hotkey('ctrl', 'v')  # ��ϼ�
        time.sleep(2)
        pyautogui.press('enter')
