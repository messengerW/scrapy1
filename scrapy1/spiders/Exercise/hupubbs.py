"""
    File   : hupubbs.py
    Author : msw
    Date   : 2020/1/31 21:56
    Ps     : ...

"""
import re
import time
import scrapy
from scrapy1.items import HupuItem
from fake_useragent import UserAgent


class Hupubbs(scrapy.Spider):
    name = 'spider2'

    allowed_domains = ['bbs.hupu.com']

    start_urls = ['https://bbs.hupu.com/bxj']

    header = {
        'User-Agent': UserAgent().random,
        'Referer': 'https://bbs.hupu.com/bxj'
    }

    def parse(self, response):
        li_list = response.xpath("//*[@id='ajaxtable']/div[1]/ul/li")
        for li in li_list:
            topic = HupuItem()
            topic['title'] = li.xpath(".//div[1]/a/text()").extract_first()
            topic['author'] = li.xpath(".//div[2]/a[1]/text()").extract_first()
            topic['date'] = li.xpath(".//div[2]/a[2]/text()").extract_first()
            topic['time'] = li.xpath(".//div[3]/a/text()").extract_first()

            # 回复量/浏览量 需要处理一下
            reply_browse = li.xpath("./span/text()").extract_first()

            topic['reply'] = re.search(r'^\d+', reply_browse).group()
            topic['browse'] = re.search(r'\d+$', reply_browse).group()

            yield topic

        for i in range(2,51):
            time.sleep(3)
            next_url = self.start_urls[0] + "-" + str(i)
            # print(next_url)
            yield scrapy.Request(next_url, callback=self.parse, headers=self.header)
