# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 23:21
"""
import time
import pyautogui
import pyperclip
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 去除inforbars的具体配置
driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe', options=options)

driver.get("https://formsmarts.com/html-form-example")
driver.maximize_window()  # 最大化方便定位
time.sleep(5)  # 强制休息5秒，方便加载页面，以免定位失败

pyautogui.scroll(-550)

pyautogui.moveTo(x=630, y=660, duration=1)  # 移动到目标位置
pyautogui.click()  # 左击一下，才可以填写
pyperclip.copy('张')  # 复制内容
pyautogui.hotkey('ctrl', 'v')  # 粘贴快捷键，把内容粘贴进去

pyautogui.click(x=637, y=711, duration=1, button='left')  # 也可以直接click中填写点击的坐标
pyperclip.copy('三')
pyautogui.hotkey('ctrl', 'v')  # 粘贴快捷键，把内容粘贴进去

pyautogui.click(x=630, y=775, duration=1, button='left')  # 邮箱
pyperclip.copy('123456789@qq.com')
pyautogui.hotkey('ctrl', 'v')  # 组合键，输入内容

pyautogui.click(x=637, y=836, duration=1, button='left')
pyautogui.click(x=637, y=920, duration=1, button='left')

pyautogui.click(x=670, y=980, duration=1, button='left')  # 点击一下输入框
pyperclip.copy('这只是一个测试')  # 复制字符串
pyautogui.hotkey('ctrl', 'v')  # 粘贴快捷键

pyautogui.scroll(-200)
pyautogui.click(x=630, y=920, duration=1, button='left')  # 点击继续
