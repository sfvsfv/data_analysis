# coding=gbk
"""
作者：川川
@时间  : 2022/3/31 21:04
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 默认用主机名
    user="root",  # 默认用户名
    password="123456",  # mysql密码
    charset='utf8'  # 编码方式
)

cursor = mydb.cursor()

cursor.execute("show databases")

for x in cursor:
    print(x)

cursor.close()