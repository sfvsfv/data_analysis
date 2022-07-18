# coding=gbk
"""
作者：川川
@时间  : 2022/3/31 11:33
"""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # 默认用主机名
    user="root",  # 默认用户名
    password="123456",  # mysql密码
    charset='utf8'  # 编码方式
)

print(db)

db.close()