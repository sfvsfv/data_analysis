# coding=gbk
"""
语法： w = Label ( master, option, ... )

作者：川川
@时间  : 2022/3/16 17:56
"""
from tkinter import *

root = Tk()
root.title('大乐斗')
root.geometry('100x50')

var = StringVar()  # 文本从属于 StringVar类的控制变量
label = Label(root, textvariable=var, relief=RAISED)

var.set("欢迎来到大乐斗小游戏！")
label.pack()
root.mainloop()
