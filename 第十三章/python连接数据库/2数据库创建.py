# coding=gbk

import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # 默认用主机名
    user="root",  # 默认用户名
    password="123456"  # mysql密码
    , charset='utf8'  # 编码方式
)

cursor = db.cursor()

cursor.execute("create database student")

db.close()