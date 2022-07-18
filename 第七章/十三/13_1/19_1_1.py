# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/8 10:14
"""
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open('1.txt').read()

x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)
#mask���Ǳ�������������ѧ��ʽ���Ƶ�һ��Բ


wc = WordCloud(background_color="white",font_path="msyh.ttf", repeat=True, mask=mask)
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()