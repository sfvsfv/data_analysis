# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/16 17:48
"""
# from tkinter import *
#
# top = Tk()
# L1 = Label(top, text="���룺") #��һ�������������ڣ��ڶ�����������ʾ����
# L1.pack(side=LEFT)
# E1 = Entry(top, bd=5)
# E1.pack(side=RIGHT)
#
# top.mainloop()


# import tkinter as tk
#
# master = tk.Tk()
#
# e = tk.Entry(master)
# e.pack(padx=20, pady=20)
#
# e.delete(0, "end")
# e.insert(0, "��������")
#
# master.mainloop()


# import tkinter as tk
#
# master = tk.Tk()
# var = tk.StringVar()
# a = tk.Entry(master, textvariable=var)
# a.pack()
#
# var.set("�Ұ� Python!")
# s = var.get()
#
# master.mainloop()


import tkinter as tk

master = tk.Tk()
# c
tk.Label(master, text="�û�����").grid(row=0)
tk.Label(master, text="���룺").grid(row=1)

enter1 = tk.Entry(master)
enter2 = tk.Entry(master)
enter1.grid(row=0, column=1, padx=10, pady=5)
enter2.grid(row=1, column=1, padx=10, pady=5)


def p():
    print("�û�����%s" % enter1.get())
    print("���룺%s" % enter2.get())
    # ������������
    enter1.delete(0, "end")
    enter2.delete(0, "end")


tk.Button(master, text="��ȡ��Ϣ", width=10, command=p).grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Button(master, text="�˳�", width=10, command=master.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)

master.mainloop()
