# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 1:46
"""
# import time
# import pyautogui
#
# # 强制休息五秒，以便于运行后打开文本，把鼠标的光标放到文本中
# time.sleep(5)
# # 鼠标所在处写入内容
# pyautogui.typewrite('I love python', interval=1)


# 中文支持
import pyautogui
import pyperclip
import time

time.sleep(3)
pyperclip.copy('我爱python')
pyautogui.hotkey('ctrl', 'v')
