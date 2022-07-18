# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 1:25
"""
import pyautogui

# moveRel相对于鼠标所在位置向右移动280，再向下移动50
pyautogui.moveRel(280, 50, duration=1)

# 左键点击
pyautogui.click()

# 点击后移动到
pyautogui.moveTo(1000, 635, duration=1)


# # 默认为左击，添加参数为右击
# pyautogui.click(button="right")
#
# # 移动到指定位置
# pyautogui.moveTo(1200, 621, duration=1)
#
# # 左键
# pyautogui.click()
