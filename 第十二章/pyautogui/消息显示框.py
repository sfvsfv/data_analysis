# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 1:52
alert() 函数显示一个警报，其中我们使用“确定”按钮将标题和文本设置为空白
 .confirm() 函数显示一个确认对话框，在该对话框中我们再次将标题和文本设置为空白，并保留两个按钮“OK”和“CANCEL”按钮
 .prompt() 函数显示一个确认提示框，我们在其中再次将标题、文本和默认值（在用户开始输入之前默认写入提示框中的内容）设置为空白。最后，
 . password() 函数显示一个密码对话框，我们再次将标题和文本设置为空白，并将掩码
"""
import pyautogui

pyautogui.alert(text='python', title='p', button='确定')

pyautogui.confirm(text='java', title='j', buttons=['确定', '取消'])

pyautogui.prompt(text='c', title='c' , default='')

# 输入后用星号掩盖，也可改为别的，主要为密码

pyautogui.password(text='c++', title='c+', default='', mask='*')
