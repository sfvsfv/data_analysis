# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/10 14:35
"""
num = int(input('i������һ��������'))

m = abs(num)  # ����ֵ
if 0 < m < 10:
    print('������Ϊһλ��')
elif m >= 10 and m < 100:
    print('������Ϊ��λ��')
elif m >= 100 and m < 1000:
    print('������Ϊ��λ��')
else:
    print('����������Ϊ��λ��')
