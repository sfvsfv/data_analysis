# coding=gbk
"""
作者：川川
@时间  : 2022/3/31 23:31
"""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # 默认用主机名
    user="root",  # 默认用户名
    password="123456",  # mysql密码
    charset='utf8',  # 编码方式
    database="student"
)

cursor = db.cursor()

sql="update information set age=30 where name='jack'"
cursor.execute(sql)

db.commit()

db.close()