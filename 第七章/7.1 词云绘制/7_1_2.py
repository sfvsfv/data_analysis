# coding=gbk
"""
���ߣ�����
@ʱ��  : 2023/12/8 10:36
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ��ȡ�ļ�
text = open('1.txt').read()

# ���������ɶ���
wc = WordCloud(font_path="msyh.ttf").generate(text=text)

# ��ʾ�����õĴ���
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# �����ļ�Ϊpng��ʽ
wc.to_file('test.png')