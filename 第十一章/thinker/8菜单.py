# coding=gbk
"""
作者：川川
@时间  : 2022/3/16 18:00
"""
from tkinter import *


# 定义每个按钮的功能
def no():
    file = Toplevel(root)
    button = Button(file, text="什么功能都没有！")
    button.pack()


root = Tk()

menu = Menu(root)  # 创建菜单对象
filemenu = Menu(menu, tearoff=0)  # tearof一般设置为0
# add_command将菜单项添加到菜单.label为名称，command为执行功能
filemenu.add_command(label="New Project", command=no)
filemenu.add_command(label="New", command=no)
filemenu.add_command(label="Open", command=no)
filemenu.add_command(label="Close", command=no)
filemenu.add_command(label="Save As", command=no)
# add_cascade通过将给定菜单与父菜单关联来创建新的分层菜单
menu.add_cascade(label="File", menu=filemenu)


# add_separator在菜单中添加分隔线，
filemenu.add_separator()
# 创建新的菜单
editmenu = Menu(menu, tearoff=0)
# 添加其它的选项
editmenu.add_command(label="Cut", command=no)
editmenu.add_command(label="Copy", command=no)
editmenu.add_command(label="Paste", command=no)
editmenu.add_command(label="Delete", command=no)
editmenu.add_command(label="Select All", command=no)
# 菜单项添加分割线
menu.add_cascade(label="Edit", menu=editmenu)

# # 在菜单中添加分隔线，
# editmenu.add_separator()
#
# # 创建新的菜单
# helpmenu = Menu(menubar, tearoff=0)
# # 添加选项
# helpmenu.add_command(label="Help Index", command=no)
# helpmenu.add_command(label="About.", command=no)
# # 添加分割
# menubar.add_cascade(label="Help", menu=helpmenu)

# 对菜单进行配置
root.config(menu=menu)
# 进入循环
root.mainloop()
