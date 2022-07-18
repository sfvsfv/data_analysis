# coding=gbk
# 导入库
from tkinter import *
import random

# 创建主窗口
root = Tk()
# 设置窗口大小
root.geometry('400x400')
root.resizable(0, 0)
# 设置标题
root.title('剪刀石头布')
root.config(bg='brown')

# 头部设置 text为显示内容，font字体，bg为背景
Label(root, text='石头剪刀布小游戏', font='Times 20 bold', bg='seashell2').pack()

# ##用户选择，文本类
user_take = StringVar()
# text为显示内容，font字体，bg背景，place显示位置
Label(root, text='选择输入一个: rock, paper ,scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
# Entry为添加输入口，字体font ，文本为选择内容，bg为背景，place为位置
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)

# 电脑选择，随机一个
com = random.randint(1, 3)
if com == 1:
    com_pick = 'rock'
elif com == 2:
    com_pick = 'paper'
else:
    com_pick = 'scissors'

##开始玩的功能
Result = StringVar()


def play():
    # user_take.get获取内容
    user_pick = user_take.get()
    # 开始进行比较
    if user_pick == com_pick:
        Result.set('平局')
    elif user_pick == 'rock' and com_pick == 'paper':
        Result.set('你输了')
    elif user_pick == 'rock' and com_pick == 'scissors':
        Result.set('你赢了')
    elif user_pick == 'paper' and com_pick == 'scissors':
        Result.set('你输了')
    elif user_pick == 'paper' and com_pick == 'rock':
        Result.set('你赢了')
    elif user_pick == 'scissors' and com_pick == 'rock':
        Result.set('你输了')
    elif user_pick == 'scissors' and com_pick == 'paper':
        Result.set('你赢了')
    else:
        Result.set('输入无效，请输入正确选项！')


##重置功能
def Reset():
    # 结果和用户输入出都设置为空
    Result.set("")
    user_take.set("")


#
#
##结束功能
def Exit():
    # 销毁窗口
    root.destroy()


#
###### 按钮设置，command为执行功能，play为所在位置，text为显示内容,bg为背景
# 输入显示框
Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50, ).place(x=25, y=250)
# 开始玩的按钮
Button(root, font='arial 13 bold', text='开始', padx=6, bg='seashell4', command=play).place(x=150, y=190)
# 重置按钮
Button(root, font='arial 13 bold', text='重置', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)
# 结束按钮
Button(root, font='arial 13 bold', text='关闭', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)

# 进入循环事件
root.mainloop()
