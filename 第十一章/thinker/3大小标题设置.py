# coding=gbk
"""
大小设置：geometry设置宽和高
作者：川川
@时间  : 2022/3/16 16:49
"""
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('GUI')
root.geometry('300x200')


# 定义一个功能
def song():
    # 第一个参数：点击后的新窗口标题，第二个参数：点击后新窗口显示内容
    msg = messagebox.showinfo('message', '你最棒了！')
    return msg


b = Button(root, text='点我', command=song)  # 第一个参数：主窗口，第二个参数：点击按钮显示内容，第三个参数：执行的函数功能
b.place(x=100, y=50)  # 按钮位置
root.mainloop()  # 进入循环，保证不会马上闪退
