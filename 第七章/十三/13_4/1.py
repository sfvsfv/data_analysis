# coding=gbk
"""
作者：川川
@时间  : 2022/3/9 0:44
"""
from icrawler.builtin import BingImageCrawler

# 需要爬取的关键字
list_word = ['宝马车','奔驰车']

filters = dict(
    size='large',
    color='color',
    license='commercial,modify',
    date='pastyear'
)

for word in list_word:
    # bing爬虫
    # 保存路径
    bing_storage = {'root_dir': 'photo\\' + word}  # photo为主文件名
    # 从上到下依次是解析器线程数，下载线程数，还有上面设置的保存路径
    bing_crawler = BingImageCrawler(parser_threads=4,
                                    downloader_threads=8,
                                    storage=bing_storage)
    # 开始爬虫，关键字+图片数量
    bing_crawler.crawl(keyword=word,
                       filters=filters,
                       max_num=10)
