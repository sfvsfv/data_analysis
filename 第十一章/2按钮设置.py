# coding=gbk
"""
按钮部件
w = Button ( root），root指的最初窗口。其它的选项可以不用传入，表示默认。

作者：川川
@时间  : 2022/3/16 16:44
"""
# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
#
#
# # 定义一个功能
# def song():
#     # 第一个参数：点击后的新窗口标题，第二个参数：点击后新窗口显示内容
#     msg = messagebox.showinfo('message', '你最棒了！')
#     return msg
#
#
# b = Button(root, text='点我', command=song)  # 第一个参数：主窗口，第二个参数：点击按钮显示内容，第三个参数：执行的函数功能
# b.place(x=100, y=50)  # 按钮位置
# root.mainloop()  # 进入循环，保证不会马上闪退


from tkinter import *
from tkinter import messagebox

root = Tk()


# 定义一个功能
def hello():
    # 第一个参数：点击后的新窗口标题，第二个参数：点击后新窗口显示内容
    msg = messagebox.showinfo('欢迎', '欢迎光临本商店！')
    return msg


b = Button(root, text='小商店', command=hello,width=10,height =5,bg='red')
b.place(x=100, y=50)  # 按钮位置
root.mainloop()  # 进入循环，保证不会马上闪退