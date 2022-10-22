# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 1:07
"""
import pyautogui

# 前两个参数为x,y坐标；第三个参数duration为移动到坐标所需时间
pyautogui.moveTo(356, 1060, duration=2)
# click()只需在鼠标当前位置用左键单击鼠标一次。click 方法不带任何参数。
pyautogui.click()

# 移动到 (1717,352) 用2秒
pyautogui.moveTo(1717,352, duration=2)

# 鼠标点击
pyautogui.click()
