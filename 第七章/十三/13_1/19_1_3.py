# coding= gbk
import jieba  # �ִ�
import matplotlib.pyplot as plt  # ���ݿ��ӻ�
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # ����
import numpy as np  # ��ѧ����
from PIL import Image  # ����ͼƬ


def draw_cloud(text, graph, save_name):
    textfile = open(text, encoding='gbk').read()  # ��ȡ�ı�����
    wordlist = jieba.cut(textfile, cut_all=False)  # ���ķִ�
    space_list = " ".join(wordlist)  # ���Ӵ���
    backgroud = np.array(Image.open(graph))  # ��������ͼ
    mywordcloud = WordCloud(background_color="white",  # ������ɫ
                            mask=backgroud,  # д���õı���ͼ���ӱ���ͼȡ��ɫ
                            max_words=100,  # ����������
                            stopwords=STOPWORDS,  # ͣ�ô�
                            font_path="msyh.ttf",  # ����
                            max_font_size=200,  # �������ߴ�
                            random_state=50,  # ����Ƕ�
                            scale=2,
                            collocations=False,  # �����ظ�����
                            )
    mywordcloud = mywordcloud.generate(space_list)  # ���ɴ���
    ImageColorGenerator(backgroud)  # ���ɴ��Ƶ���ɫ
    plt.imsave(save_name, mywordcloud)  # ����ͼƬ
    plt.imshow(mywordcloud)  # ��ʾ����
    plt.axis("off")  # �رձ���
    plt.show()  # ��ʾ����


if __name__ == '__main__':
    draw_cloud('1.txt', graph="��Ƶ����2.png", save_name='3.png')
