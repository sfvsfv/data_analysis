# coding=gbk
"""
��ť����
w = Button ( root����rootָ��������ڡ�������ѡ����Բ��ô��룬��ʾĬ�ϡ�

���ߣ�����
@ʱ��  : 2022/3/16 16:44
"""
# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
#
#
# # ����һ������
# def song():
#     # ��һ���������������´��ڱ��⣬�ڶ���������������´�����ʾ����
#     msg = messagebox.showinfo('message', '������ˣ�')
#     return msg
#
#
# b = Button(root, text='����', command=song)  # ��һ�������������ڣ��ڶ��������������ť��ʾ���ݣ�������������ִ�еĺ�������
# b.place(x=100, y=50)  # ��ťλ��
# root.mainloop()  # ����ѭ������֤������������


from tkinter import *
from tkinter import messagebox

root = Tk()


# ����һ������
def hello():
    # ��һ���������������´��ڱ��⣬�ڶ���������������´�����ʾ����
    msg = messagebox.showinfo('��ӭ', '��ӭ���ٱ��̵꣡')
    return msg


b = Button(root, text='С�̵�', command=hello,width=10,height =5,bg='red')
b.place(x=100, y=50)  # ��ťλ��
root.mainloop()  # ����ѭ������֤������������