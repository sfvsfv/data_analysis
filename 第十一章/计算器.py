# coding=gbk
from tkinter import *
import parser
from math import factorial

root = Tk()
root.title('计算器')
root.geometry('480x480')

# 它跟踪输入文本字段上的当前位置
i = 0


# 接收数字作为参数并将其显示在输入字段上
def get_value(num):
    global i
    # 插入到第几个位置
    display.insert(i, num)
    i += 1


# 计算函数扫描字符串以得到结果并显示它
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()  # 解析输入字符串，传入eval
        result = eval(a)
        # 得到结果后清空，把结果插入到第一个位置
        clear_all()
        display.insert(0, result)
    except Exception:
        # 斗则清空，在第一个位置显示出错
        clear_all()
        display.insert(0, "出错")


# 将运算符作为输入并显示在输入字段上的函数
def get_operation(oper):
    global i
    length = len(oper)
    display.insert(i, oper)
    i += length


# 清除输入字段的功能
def clear_all():
    display.delete(0, END)


#
# 类似于退格的功能
def qingchu():
    # 获取
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()  # 清空函数
        # 把新的内容插入回来
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "出错")


# 计算阶乘并显示的函数
def fact():
    # 获取
    entire_string = display.get()
    try:
        # 计算
        result = factorial(int(entire_string))
        # 计算后清空
        clear_all()
        # 把结果插入到第一个位置
        display.insert(0, result)
    except Exception:
        # 否则清空并显示出错
        clear_all()
        display.insert(0, "出错")


# --------------------------------------UI 设计 ---------------------------------------------

# 添加输入框
# columnspan：表示占用几列 columnspan=6，表示这个部件占用6列
# rowspan表示占用几行 rowspan=1，表示这个部件占用1列
display = Entry(root)
display.grid(rowspan=1, columnspan=6, sticky=N + E + W + S, padx=0, pady=0)

# 添加按钮
# 添加数字
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

# 添加符号
Button(root, text="清空", width=10, height=5, command=lambda: clear_all()).grid(row=5, column=0, sticky=N + S + E + W)
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

# 添加高级点的符号
Button(root, text="pi", width=10, height=5, command=lambda: get_operation("3.14")).grid(row=2, column=4,
                                                                                        sticky=N + S + E + W)
Button(root, text="%", width=10, height=5, command=lambda: get_operation("%")).grid(row=3, column=4,
                                                                                    sticky=N + S + E + W)
Button(root, text="(", width=10, height=5, command=lambda: get_operation("(")).grid(row=4, column=4,
                                                                                    sticky=N + S + E + W)
Button(root, text="exp", width=10, height=5, command=lambda: get_operation("**")).grid(row=5, column=4,
                                                                                       sticky=N + S + E + W)

Button(root, text="删除", width=10, height=5, command=lambda: qingchu()).grid(row=2, column=5, sticky=N + S + E + W)
Button(root, text="x!", width=10, height=5, command=lambda: fact()).grid(row=3, column=5, sticky=N + S + E + W)
Button(root, text=")", width=10, height=5, command=lambda: get_operation(")")).grid(row=4, column=5,
                                                                                    sticky=N + S + E + W)
Button(root, text="^2", width=10, height=5, command=lambda: get_operation("**2")).grid(row=5, column=5,
                                                                                       sticky=N + S + E + W)
Button(root, text="^2", width=10, height=5, command=lambda: get_operation("**2")).grid(row=5, column=5,
                                                                                       sticky=N + S + E + W)
Button(root, text="=", width=10, height=5, command=lambda: calculate()).grid(columnspan=6, sticky=N + S + E + W)

root.mainloop()
