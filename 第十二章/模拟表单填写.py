# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 23:21
"""
import time
import pyautogui
import pyperclip
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])  # ȥ��inforbars�ľ�������
driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe', options=options)

driver.get("https://formsmarts.com/html-form-example")
driver.maximize_window()  # ��󻯷��㶨λ
time.sleep(5)  # ǿ����Ϣ5�룬�������ҳ�棬���ⶨλʧ��

pyautogui.scroll(-550)

pyautogui.moveTo(x=630, y=660, duration=1)  # �ƶ���Ŀ��λ��
pyautogui.click()  # ���һ�£��ſ�����д
pyperclip.copy('��')  # ��������
pyautogui.hotkey('ctrl', 'v')  # ճ����ݼ���������ճ����ȥ

pyautogui.click(x=637, y=711, duration=1, button='left')  # Ҳ����ֱ��click����д���������
pyperclip.copy('��')
pyautogui.hotkey('ctrl', 'v')  # ճ����ݼ���������ճ����ȥ

pyautogui.click(x=630, y=775, duration=1, button='left')  # ����
pyperclip.copy('123456789@qq.com')
pyautogui.hotkey('ctrl', 'v')  # ��ϼ�����������

pyautogui.click(x=637, y=836, duration=1, button='left')
pyautogui.click(x=637, y=920, duration=1, button='left')

pyautogui.click(x=670, y=980, duration=1, button='left')  # ���һ�������
pyperclip.copy('��ֻ��һ������')  # �����ַ���
pyautogui.hotkey('ctrl', 'v')  # ճ����ݼ�

pyautogui.scroll(-200)
pyautogui.click(x=630, y=920, duration=1, button='left')  # �������
