# coding=gbk
"""
�����﷨��w = Checkbutton ( master, option, ... )
master - ��������ڡ�
options - ���Ǵ�С������õ�ѡ���б���Щѡ����������Զ��ŷָ��ļ�ֵ�ԡ�
���ߣ�����
@ʱ��  : 2022/3/16 16:58
"""

from tkinter import *

top = Tk()
top.title('��ѡ')
top.geometry('300x300')

# ��ť���ã�topΪ�����ڣ�textΪ��ť���⣬variable���ټ�鰴ť��ǰ״̬��ͨ�����������һ��IntVar
# onvalueһ������Ϊ1����ʾ��ѡ�����Ϊ0��ʾ�̶���ѡ��offvalueһ������Ϊ0��heigh�ߣ�width��.��������Ĭ�ϼ��ɡ�

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
