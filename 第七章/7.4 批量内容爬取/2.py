# coding=gbk
"""
作者：川川
@时间  : 2023/12/9 10:17
"""
from icrawler.builtin import GreedyImageCrawler

greedy_crawler = GreedyImageCrawler(storage={'root_dir': 'photo//girl//'})
greedy_crawler.crawl(domains='https://desk.3gbizhi.com/deskMV/', max_num=10,
                     min_size=None, max_size=None)

