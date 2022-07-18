# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 2:27
"""
import pyautogui
import time
# 添加confidence能更加精确，不然似乎不是很能精准，需要有opencv
# a = pyautogui.locateOnScreen('wei.png', confidence=0.9)
# print(a)
l, t, w, h = pyautogui.locateOnScreen('t.png', confidence=0.9)
pyautogui.moveTo(l, t+50, duration=1)
# time.sleep(2)
# pyautogui.doubleClick()
# print(l)
# print(t)
# print(w)
# print(h)

# 添加confidence才定位到
# x,y= pyautogui.locateCenterOnScreen('wei.png',confidence=0.9)
# print(x)
# print(y)
