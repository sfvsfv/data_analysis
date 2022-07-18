# coding=gbk
"""
作者：川川
@时间  : 2022/3/31 21:50
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
''' 单个数据插入'''
# sql="insert into information values ('jack','boy',20)"
# cursor.execute(sql)


''' 多条数据插入 '''
sql = "insert into information (name, sex,age) values (%s,%s,%s)"
val = (
    ('mark', 'boy', 21),
    ('json', 'boy', 20),
    ('mary', 'girl', 18)
)

cursor.executemany(sql, val)


# 在数据库中提交你的更改
db.commit()

# 打印数据的行数
print(cursor.rowcount, "全部添加成功.")

db.close()

