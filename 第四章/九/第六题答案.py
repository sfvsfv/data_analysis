# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/4/10 14:48
"""
a, b, c = map(int, input('�������������֣��ո�ֿ���').split())
if a + b > c and a + c > b and b + c > a:
    print('�����������')
    if a == b or a == c or b == c:
        print('���һ��ǵ���������')
    else:
        print('���ǲ�����ɵ���������')
else:
    print('�������������')
