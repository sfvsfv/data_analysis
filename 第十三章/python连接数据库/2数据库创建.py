# coding=gbk

import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # Ĭ����������
    user="root",  # Ĭ���û���
    password="123456"  # mysql����
    , charset='utf8'  # ���뷽ʽ
)

cursor = db.cursor()

cursor.execute("create database student")

db.close()