# coding=gbk
# �����
from tkinter import *
import random

# ����������
root = Tk()
# ���ô��ڴ�С
root.geometry('400x400')
root.resizable(0, 0)
# ���ñ���
root.title('����ʯͷ��')
root.config(bg='brown')

# ͷ������ textΪ��ʾ���ݣ�font���壬bgΪ����
Label(root, text='ʯͷ������С��Ϸ', font='Times 20 bold', bg='seashell2').pack()

# ##�û�ѡ���ı���
user_take = StringVar()
# textΪ��ʾ���ݣ�font���壬bg������place��ʾλ��
Label(root, text='ѡ������һ��: rock, paper ,scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
# EntryΪ�������ڣ�����font ���ı�Ϊѡ�����ݣ�bgΪ������placeΪλ��
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)

# ����ѡ�����һ��
com = random.randint(1, 3)
if com == 1:
    com_pick = 'rock'
elif com == 2:
    com_pick = 'paper'
else:
    com_pick = 'scissors'

##��ʼ��Ĺ���
Result = StringVar()


def play():
    # user_take.get��ȡ����
    user_pick = user_take.get()
    # ��ʼ���бȽ�
    if user_pick == com_pick:
        Result.set('ƽ��')
    elif user_pick == 'rock' and com_pick == 'paper':
        Result.set('������')
    elif user_pick == 'rock' and com_pick == 'scissors':
        Result.set('��Ӯ��')
    elif user_pick == 'paper' and com_pick == 'scissors':
        Result.set('������')
    elif user_pick == 'paper' and com_pick == 'rock':
        Result.set('��Ӯ��')
    elif user_pick == 'scissors' and com_pick == 'rock':
        Result.set('������')
    elif user_pick == 'scissors' and com_pick == 'paper':
        Result.set('��Ӯ��')
    else:
        Result.set('������Ч����������ȷѡ�')


##���ù���
def Reset():
    # ������û������������Ϊ��
    Result.set("")
    user_take.set("")


#
#
##��������
def Exit():
    # ���ٴ���
    root.destroy()


#
###### ��ť���ã�commandΪִ�й��ܣ�playΪ����λ�ã�textΪ��ʾ����,bgΪ����
# ������ʾ��
Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50, ).place(x=25, y=250)
# ��ʼ��İ�ť
Button(root, font='arial 13 bold', text='��ʼ', padx=6, bg='seashell4', command=play).place(x=150, y=190)
# ���ð�ť
Button(root, font='arial 13 bold', text='����', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)
# ������ť
Button(root, font='arial 13 bold', text='�ر�', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)

# ����ѭ���¼�
root.mainloop()
