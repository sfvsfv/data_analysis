# coding=gbk
"""
作者：川川
@时间  : 2022/4/8 8:45
"""


def hello(text):
    return text.upper()


def not_hello(text):
    return text.lower()


def greet(func):
    greeting = func("""hello world""")
    print(greeting)


greet(hello)
greet(not_hello)
