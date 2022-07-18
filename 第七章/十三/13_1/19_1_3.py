# coding= gbk
import jieba  # 分词
import matplotlib.pyplot as plt  # 数据可视化
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # 词云
import numpy as np  # 科学计算
from PIL import Image  # 处理图片


def draw_cloud(text, graph, save_name):
    textfile = open(text, encoding='gbk').read()  # 读取文本内容
    wordlist = jieba.cut(textfile, cut_all=False)  # 中文分词
    space_list = " ".join(wordlist)  # 连接词语
    backgroud = np.array(Image.open(graph))  # 背景轮廓图
    mywordcloud = WordCloud(background_color="white",  # 背景颜色
                            mask=backgroud,  # 写字用的背景图，从背景图取颜色
                            max_words=100,  # 最大词语数量
                            stopwords=STOPWORDS,  # 停用词
                            font_path="msyh.ttf",  # 字体
                            max_font_size=200,  # 最大字体尺寸
                            random_state=50,  # 随机角度
                            scale=2,
                            collocations=False,  # 避免重复单词
                            )
    mywordcloud = mywordcloud.generate(space_list)  # 生成词云
    ImageColorGenerator(backgroud)  # 生成词云的颜色
    plt.imsave(save_name, mywordcloud)  # 保存图片
    plt.imshow(mywordcloud)  # 显示词云
    plt.axis("off")  # 关闭保存
    plt.show()  # 显示词云


if __name__ == '__main__':
    draw_cloud('1.txt', graph="词频背景2.png", save_name='3.png')
