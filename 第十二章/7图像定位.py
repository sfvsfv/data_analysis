# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 2:27
"""
import pyautogui
import time
# ���confidence�ܸ��Ӿ�ȷ����Ȼ�ƺ����Ǻ��ܾ�׼����Ҫ��opencv
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

# ���confidence�Ŷ�λ��
# x,y= pyautogui.locateCenterOnScreen('wei.png',confidence=0.9)
# print(x)
# print(y)
