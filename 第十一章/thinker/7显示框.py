# coding=gbk
"""
�﷨�� w = Label ( master, option, ... )

���ߣ�����
@ʱ��  : 2022/3/16 17:56
"""
from tkinter import *

root = Tk()
root.title('���ֶ�')
root.geometry('100x50')

var = StringVar()  # �ı������� StringVar��Ŀ��Ʊ���
label = Label(root, textvariable=var, relief=RAISED)

var.set("��ӭ�������ֶ�С��Ϸ��")
label.pack()
root.mainloop()
