# coding=gbk
"""
��С���ã�geometry���ÿ�͸�
���ߣ�����
@ʱ��  : 2022/3/16 16:49
"""
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('GUI')
root.geometry('300x200')


# ����һ������
def song():
    # ��һ���������������´��ڱ��⣬�ڶ���������������´�����ʾ����
    msg = messagebox.showinfo('message', '������ˣ�')
    return msg


b = Button(root, text='����', command=song)  # ��һ�������������ڣ��ڶ��������������ť��ʾ���ݣ�������������ִ�еĺ�������
b.place(x=100, y=50)  # ��ťλ��
root.mainloop()  # ����ѭ������֤������������
