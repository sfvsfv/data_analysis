# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 1:46
"""
# import time
# import pyautogui
#
# # ǿ����Ϣ���룬�Ա������к���ı��������Ĺ��ŵ��ı���
# time.sleep(5)
# # ������ڴ�д������
# pyautogui.typewrite('I love python', interval=1)


# ����֧��
import pyautogui
import pyperclip
import time

time.sleep(3)
pyperclip.copy('�Ұ�python')
pyautogui.hotkey('ctrl', 'v')
