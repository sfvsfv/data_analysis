# coding=gbk
"""
�﷨��w = Frame ( master, option, ... )
pack:���ι������ڽ�С�������븸С����֮ǰ��������֯�ɿ顣side - ȷ����С��������һ������TOP��Ĭ�ϣ���BOTTOM��LEFT �� RIGHT��
���ߣ�����
@ʱ��  : 2022/3/16 17:52
"""
from tkinter import *

root = Tk()
root.geometry('300x200')
root.title('����')
# ����һ������
frame1 = Frame(root)
frame1.pack()

# �����ڶ���������ǿ�������ڵײ�
frame2 = Frame(root)
frame2.pack(side=BOTTOM)

#ת������1��
button1 = Button(frame1, text="python", fg="red")
button1.pack(side=LEFT)

button2 = Button(frame1, text="java", fg="brown")
button2.pack(side=LEFT)
#ת������2��
button3 = Button(frame2, text="C", fg="blue")
button3.pack(side=BOTTOM)

button4 = Button(frame2, text="C++", fg="black")
button4.pack(side=BOTTOM)

root.mainloop()
