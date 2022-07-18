# coding=gbk
"""
作者：川川
@时间  : 2022/3/8 10:14
"""
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open('1.txt').read()

x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)
#mask就是背景，这里用数学公式绘制的一个圆


wc = WordCloud(background_color="white",font_path="msyh.ttf", repeat=True, mask=mask)
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()