# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/16 18:00
"""
from tkinter import *


# ����ÿ����ť�Ĺ���
def no():
    file = Toplevel(root)
    button = Button(file, text="ʲô���ܶ�û�У�")
    button.pack()


root = Tk()

menu = Menu(root)  # �����˵�����
filemenu = Menu(menu, tearoff=0)  # tearofһ������Ϊ0
# add_command���˵�����ӵ��˵�.labelΪ���ƣ�commandΪִ�й���
filemenu.add_command(label="New Project", command=no)
filemenu.add_command(label="New", command=no)
filemenu.add_command(label="Open", command=no)
filemenu.add_command(label="Close", command=no)
filemenu.add_command(label="Save As", command=no)
# add_cascadeͨ���������˵��븸�˵������������µķֲ�˵�
menu.add_cascade(label="File", menu=filemenu)


# add_separator�ڲ˵�����ӷָ��ߣ�
filemenu.add_separator()
# �����µĲ˵�
editmenu = Menu(menu, tearoff=0)
# ���������ѡ��
editmenu.add_command(label="Cut", command=no)
editmenu.add_command(label="Copy", command=no)
editmenu.add_command(label="Paste", command=no)
editmenu.add_command(label="Delete", command=no)
editmenu.add_command(label="Select All", command=no)
# �˵�����ӷָ���
menu.add_cascade(label="Edit", menu=editmenu)

# # �ڲ˵�����ӷָ��ߣ�
# editmenu.add_separator()
#
# # �����µĲ˵�
# helpmenu = Menu(menubar, tearoff=0)
# # ���ѡ��
# helpmenu.add_command(label="Help Index", command=no)
# helpmenu.add_command(label="About.", command=no)
# # ��ӷָ�
# menubar.add_cascade(label="Help", menu=helpmenu)

# �Բ˵���������
root.config(menu=menu)
# ����ѭ��
root.mainloop()
