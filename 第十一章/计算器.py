# coding=gbk
from tkinter import *
import parser
from math import factorial

root = Tk()
root.title('������')
root.geometry('480x480')

# �����������ı��ֶ��ϵĵ�ǰλ��
i = 0


# ����������Ϊ������������ʾ�������ֶ���
def get_value(num):
    global i
    # ���뵽�ڼ���λ��
    display.insert(i, num)
    i += 1


# ���㺯��ɨ���ַ����Եõ��������ʾ��
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()  # ���������ַ���������eval
        result = eval(a)
        # �õ��������գ��ѽ�����뵽��һ��λ��
        clear_all()
        display.insert(0, result)
    except Exception:
        # ������գ��ڵ�һ��λ����ʾ����
        clear_all()
        display.insert(0, "����")


# ���������Ϊ���벢��ʾ�������ֶ��ϵĺ���
def get_operation(oper):
    global i
    length = len(oper)
    display.insert(i, oper)
    i += length


# ��������ֶεĹ���
def clear_all():
    display.delete(0, END)


#
# �������˸�Ĺ���
def qingchu():
    # ��ȡ
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()  # ��պ���
        # ���µ����ݲ������
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "����")


# ����׳˲���ʾ�ĺ���
def fact():
    # ��ȡ
    entire_string = display.get()
    try:
        # ����
        result = factorial(int(entire_string))
        # ��������
        clear_all()
        # �ѽ�����뵽��һ��λ��
        display.insert(0, result)
    except Exception:
        # ������ղ���ʾ����
        clear_all()
        display.insert(0, "����")


# --------------------------------------UI ��� ---------------------------------------------

# ��������
# columnspan����ʾռ�ü��� columnspan=6����ʾ�������ռ��6��
# rowspan��ʾռ�ü��� rowspan=1����ʾ�������ռ��1��
display = Entry(root)
display.grid(rowspan=1, columnspan=6, sticky=N + E + W + S, padx=0, pady=0)

# ��Ӱ�ť
# �������
Button(root, text="1", width=10, height=5, command=lambda: get_value(1)).grid(row=2, column=0, sticky=N + S + E + W)
Button(root, text=" 2", width=10, height=5, command=lambda: get_value(2)).grid(row=2, column=1, sticky=N + S + E + W)
Button(root, text=" 3", width=10, height=5, command=lambda: get_value(3)).grid(row=2, column=2, sticky=N + S + E + W)

Button(root, text="4", width=10, height=5, command=lambda: get_value(4)).grid(row=3, column=0, sticky=N + S + E + W)
Button(root, text=" 5", width=10, height=5, command=lambda: get_value(5)).grid(row=3, column=1, sticky=N + S + E + W)
Button(root, text=" 6", width=10, height=5, command=lambda: get_value(6)).grid(row=3, column=2, sticky=N + S + E + W)

Button(root, text="7", width=10, height=5, command=lambda: get_value(7)).grid(row=4, column=0, sticky=N + S + E + W)
Button(root, text=" 8", width=10, height=5, command=lambda: get_value(8)).grid(row=4, column=1, sticky=N + S + E + W)
Button(root, text=" 9", width=10, height=5, command=lambda: get_value(9)).grid(row=4, column=2,
                                                                               sticky=N + S + E + W)

# ��ӷ���
Button(root, text="���", width=10, height=5, command=lambda: clear_all()).grid(row=5, column=0, sticky=N + S + E + W)
Button(root, text=" 0", width=10, height=5, command=lambda: get_value(0)).grid(row=5, column=1, sticky=N + S + E + W)
Button(root, text=" .", width=10, height=5, command=lambda: get_value(".")).grid(row=5, column=2, sticky=N + S + E + W)

Button(root, text="+", width=10, height=5, command=lambda: get_operation("+")).grid(row=2, column=3,
                                                                                    sticky=N + S + E + W)
Button(root, text="-", width=10, height=5, command=lambda: get_operation("-")).grid(row=3, column=3,
                                                                                    sticky=N + S + E + W)
Button(root, text="*", width=10, height=5, command=lambda: get_operation("*")).grid(row=4, column=3,
                                                                                    sticky=N + S + E + W)
Button(root, text="/", width=10, height=5, command=lambda: get_operation("/")).grid(row=5, column=3,
                                                                                    sticky=N + S + E + W)

# ��Ӹ߼���ķ���
Button(root, text="pi", width=10, height=5, command=lambda: get_operation("3.14")).grid(row=2, column=4,
                                                                                        sticky=N + S + E + W)
Button(root, text="%", width=10, height=5, command=lambda: get_operation("%")).grid(row=3, column=4,
                                                                                    sticky=N + S + E + W)
Button(root, text="(", width=10, height=5, command=lambda: get_operation("(")).grid(row=4, column=4,
                                                                                    sticky=N + S + E + W)
Button(root, text="exp", width=10, height=5, command=lambda: get_operation("**")).grid(row=5, column=4,
                                                                                       sticky=N + S + E + W)

Button(root, text="ɾ��", width=10, height=5, command=lambda: qingchu()).grid(row=2, column=5, sticky=N + S + E + W)
Button(root, text="x!", width=10, height=5, command=lambda: fact()).grid(row=3, column=5, sticky=N + S + E + W)
Button(root, text=")", width=10, height=5, command=lambda: get_operation(")")).grid(row=4, column=5,
                                                                                    sticky=N + S + E + W)
Button(root, text="^2", width=10, height=5, command=lambda: get_operation("**2")).grid(row=5, column=5,
                                                                                       sticky=N + S + E + W)
Button(root, text="^2", width=10, height=5, command=lambda: get_operation("**2")).grid(row=5, column=5,
                                                                                       sticky=N + S + E + W)
Button(root, text="=", width=10, height=5, command=lambda: calculate()).grid(columnspan=6, sticky=N + S + E + W)

root.mainloop()
