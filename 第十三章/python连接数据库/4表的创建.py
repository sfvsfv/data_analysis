# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/31 21:22
"""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # Ĭ����������
    user="root",  # Ĭ���û���
    password="123456",  # mysql����
    charset='utf8',  # ���뷽ʽ
    database="student"  # ���ݿ�����
)

cursor = db.cursor()

cursor.execute('create table information(name varchar(255),sex varchar(255),age int(3))')
# ִ�в�������Ҫ��commit�ύ���ݿⷢ�����
db.commit()

print('�����ɹ�...')
db.close()
