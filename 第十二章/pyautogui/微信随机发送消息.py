# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 23:01
"""
import pyautogui
import time
import pyperclip
pyautogui.moveTo(394, 1068, duration=0.5)

pyautogui.click(clicks=1,button='left')

li=['你知道吗？你很特别，和别的女孩不一样','你身上散发出的气质 很令我着迷','这件衣服很普通，但穿在你身上很有味道']
for i in range(3):
    for j in li:
        pyperclip.copy(j)
        pyautogui.hotkey('ctrl', 'v')  # 组合键
        time.sleep(2)
        pyautogui.press('enter')
