# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 20:59
"""

import pyautogui
import time

pyautogui.moveTo(394, 1068, duration=0.5)

pyautogui.click(clicks=1,button='left')


for i in range(3):
    pyautogui.typewrite('����һ��test')
    time.sleep(2)
    pyautogui.press('enter')

