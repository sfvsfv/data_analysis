# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/19 1:52
alert() ������ʾһ����������������ʹ�á�ȷ������ť��������ı�����Ϊ�հ�
 .confirm() ������ʾһ��ȷ�϶Ի����ڸöԻ����������ٴν�������ı�����Ϊ�հף�������������ť��OK���͡�CANCEL����ť
 .prompt() ������ʾһ��ȷ����ʾ�������������ٴν����⡢�ı���Ĭ��ֵ�����û���ʼ����֮ǰĬ��д����ʾ���е����ݣ�����Ϊ�հס����
 . password() ������ʾһ������Ի��������ٴν�������ı�����Ϊ�հף���������
"""
import pyautogui

pyautogui.alert(text='python', title='p', button='ȷ��')

pyautogui.confirm(text='java', title='j', buttons=['ȷ��', 'ȡ��'])

pyautogui.prompt(text='c', title='c' , default='')

# ��������Ǻ��ڸǣ�Ҳ�ɸ�Ϊ��ģ���ҪΪ����

pyautogui.password(text='c++', title='c+', default='', mask='*')
