# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/31 21:04
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # Ĭ����������
    user="root",  # Ĭ���û���
    password="123456",  # mysql����
    charset='utf8'  # ���뷽ʽ
)

cursor = mydb.cursor()

cursor.execute("show databases")

for x in cursor:
    print(x)

cursor.close()