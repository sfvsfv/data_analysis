# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/31 21:50
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
''' �������ݲ���'''
# sql="insert into information values ('jack','boy',20)"
# cursor.execute(sql)


''' �������ݲ��� '''
sql = "insert into information (name, sex,age) values (%s,%s,%s)"
val = (
    ('mark', 'boy', 21),
    ('json', 'boy', 20),
    ('mary', 'girl', 18)
)

cursor.executemany(sql, val)


# �����ݿ����ύ��ĸ���
db.commit()

# ��ӡ���ݵ�����
print(cursor.rowcount, "ȫ����ӳɹ�.")

db.close()

