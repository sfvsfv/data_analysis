# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 20:21
"""
from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe')

driver.get('https://blog.csdn.net/rank/list')
driver.maximize_window()

time.sleep(2)
pyautogui.scroll(-1000)
time.sleep(3)
pyautogui.scroll(-1000)
time.sleep(3)
pyautogui.scroll(-1000)
time.sleep(3)
pyautogui.scroll(-1000)
