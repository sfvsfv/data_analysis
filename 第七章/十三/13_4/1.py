# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/9 0:44
"""
from icrawler.builtin import BingImageCrawler

# ��Ҫ��ȡ�Ĺؼ���
list_word = ['����','���۳�']

filters = dict(
    size='large',
    color='color',
    license='commercial,modify',
    date='pastyear'
)

for word in list_word:
    # bing����
    # ����·��
    bing_storage = {'root_dir': 'photo\\' + word}  # photoΪ���ļ���
    # ���ϵ��������ǽ������߳����������߳����������������õı���·��
    bing_crawler = BingImageCrawler(parser_threads=4,
                                    downloader_threads=8,
                                    storage=bing_storage)
    # ��ʼ���棬�ؼ���+ͼƬ����
    bing_crawler.crawl(keyword=word,
                       filters=filters,
                       max_num=10)
