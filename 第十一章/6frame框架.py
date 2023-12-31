# coding=gbk
"""
语法：w = Frame ( master, option, ... )
pack:几何管理器在将小部件放入父小部件之前将它们组织成块。side - 确定父小部件的哪一侧打包：TOP（默认）、BOTTOM、LEFT 或 RIGHT。
作者：川川
@时间  : 2022/3/16 17:52
"""
from tkinter import *

root = Tk()
root.geometry('300x200')
root.title('容器')
# 创建一个容器
frame1 = Frame(root)
frame1.pack()

# 创建第二个容器，强调必须在底部
frame2 = Frame(root)
frame2.pack(side=BOTTOM)

#转载容器1中
button1 = Button(frame1, text="python", fg="red")
button1.pack(side=LEFT)

button2 = Button(frame1, text="java", fg="brown")
button2.pack(side=LEFT)
#转载容器2中
button3 = Button(frame2, text="C", fg="blue")
button3.pack(side=BOTTOM)

button4 = Button(frame2, text="C++", fg="black")
button4.pack(side=BOTTOM)

root.mainloop()
