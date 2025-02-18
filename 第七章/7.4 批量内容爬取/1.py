# coding=gbk
"""
作者：川川
@时间  : 202/02/18 0:44
"""
# pip install beautifulsoup4  icrawler
import os
from icrawler.builtin import BingImageCrawler

# 需要爬取的关键字
list_word = ['比亚迪汽车']

# 确保路径存在
if not os.path.exists('photo'):
    os.makedirs('photo')

for word in list_word:
    # 保存路径
    bing_storage = {'root_dir': os.path.join('photo', word)}  # 使用os.path.join处理路径

    # 创建BingImageCrawler实例
    bing_crawler = BingImageCrawler(
        parser_threads=3,  # 使用3个解析线程
        downloader_threads=4,  # 使用4个下载线程
        storage=bing_storage
    )

    # 开始爬虫，关键字+图片数量
    bing_crawler.crawl(
        keyword=word,  # 关键字
        max_num=10  # 最大下载10张图片
    )
