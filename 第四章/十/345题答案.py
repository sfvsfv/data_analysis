# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/8 0:14
"""
# ������
# count = int(input("�����������Ҫ���뼸������: "))
# i = 0
# sum = 0
# for i in range(count):
#     x = int(input("������һ������: "))
#     sum = sum + x
# avg = sum / count
# print("ƽ��ֵΪ: ", avg)


# ������
# i = 0
# res = 1
# count = int(input("�����������Ҫ���뼸������: "))
# for i in range(count):
#     x = float(input("������һ������: "))
#     res =res * x
# print("�������ֳ˻���СΪ: ", res)


# ������
count = 0
sum = 0.0
while (count < 10):
    number = float(input("������һ������: "))
    count = count + 1
    sum = sum + number
avg = sum / 10
print("ƽ��ֵ :", avg)
