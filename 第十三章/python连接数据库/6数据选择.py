# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/31 23:10
"""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # Ĭ����������
    user="root",  # Ĭ���û���
    password="123456",  # mysql����
    charset='utf8',  # ���뷽ʽ
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
print('ѡ��������:')
for i in res:
    print(i)

db.close()
