# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/10 14:40
"""
year = int(input('��������ݣ�'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('{}��Ϊ����'.format(year))
else:
    print('���겻������')
