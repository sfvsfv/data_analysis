# coding=gbk
"""
基本语法：w = Checkbutton ( master, option, ... )
master - 这代表父窗口。
options - 这是此小部件最常用的选项列表。这些选项可以用作以逗号分隔的键值对。
作者：川川
@时间  : 2022/3/16 16:58
"""

from tkinter import *

top = Tk()
top.title('复选')
top.geometry('300x300')

# 按钮设置：top为主窗口，text为按钮标题，variable跟踪检查按钮当前状态，通常这个变量是一个IntVar
# onvalue一般设置为1，表示可选，如果为0表示固定勾选；offvalue一般设置为0，heigh高，width宽.其他参数默认即可。

C1 = Checkbutton(top, text="python", variable=IntVar, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20)

C2 = Checkbutton(top, text="java", variable=IntVar, \
                 onvalue=0, offvalue=0, height=5, \
                 width=20)

C3 = Checkbutton(top, text="C++", variable=IntVar, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20)

C1.pack()
C2.pack()
C3.pack()
top.mainloop()
