# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 22:48
"""
import pyautogui
import pyperclip
import time

pyautogui.moveTo(394, 1068, duration=0.5)

pyautogui.click(clicks=1,button='left')


for i in range(2):
    time.sleep(2)
    pyperclip.copy('这是一个测试！')
    pyautogui.hotkey('ctrl', 'v')  # 组合键
    pyautogui.press('enter')