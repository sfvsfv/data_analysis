# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/16 18:29
"""
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")


def hello():
    messagebox.showinfo("˵", "Hello World")


B1 = Button(top, text="Say Hello", command=hello)
B1.place(x=35, y=50)

top.mainloop()
