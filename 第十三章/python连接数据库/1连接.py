# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/31 11:33
"""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # Ĭ����������
    user="root",  # Ĭ���û���
    password="123456",  # mysql����
    charset='utf8'  # ���뷽ʽ
)

print(db)

db.close()