# coding=gbk
"""
作者：川川
@时间  : 2022/3/31 21:22
"""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # 默认用主机名
    user="root",  # 默认用户名
    password="123456",  # mysql密码
    charset='utf8',  # 编码方式
    database="student"  # 数据库名称
)

cursor = db.cursor()

cursor.execute('create table information(name varchar(255),sex varchar(255),age int(3))')
# 执行操作后需要，commit提交数据库发生变更
db.commit()

print('创建成功...')
db.close()
