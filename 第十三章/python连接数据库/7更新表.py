# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/31 23:31
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

sql="update information set age=30 where name='jack'"
cursor.execute(sql)

db.commit()

db.close()