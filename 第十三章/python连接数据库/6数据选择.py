# coding=gbk
"""
作者：川川
@时间  : 2022/3/31 23:10
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

# sql = 'select name,age from information'
# sql='select name from information'

# sql="select * from information where name='mark'"
sql="select * from information where name like 'j%' "
cursor.execute(sql)

res = cursor.fetchall()

db.commit()
print('选择结果如下:')
for i in res:
    print(i)

db.close()
