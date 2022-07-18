# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 1:34
"""
import pyautogui

# 移动到目标位置
pyautogui.moveTo(356, 1060, duration=1)

# 左键点击
pyautogui.click()

# 移动到目标位置
pyautogui.moveTo(1077, 192, duration=1)

# 拖拽到位置（500，500）
pyautogui.dragTo(500, 500, duration=1)

# 相对现在位置向右向下移动50
pyautogui.dragRel(50, 50, duration=1)
