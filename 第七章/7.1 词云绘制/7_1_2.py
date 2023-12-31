# coding=gbk
"""
作者：川川
@时间  : 2023/12/8 10:36
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文件
text = open('1.txt').read()

# 制作并生成对象
wc = WordCloud(font_path="msyh.ttf").generate(text=text)

# 显示制作好的词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存文件为png格式
wc.to_file('test.png')