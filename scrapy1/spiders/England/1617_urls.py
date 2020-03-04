"""
    File   : 1617_urls.py
    Author : msw
    Date   : 2020-03-03 21:09
    Ps     : ...
    
"""
import re
import scrapy
from scrapy1.items import MaoItem
from fake_useragent import UserAgent

class urls(scrapy.Spider):
    name = 'spider_url'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/matches/5614/report.do']

    header = {
        'User-Agent': UserAgent().random,
    }

    url_list = []

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], headers=self.header)

    def parse(self, response):
        game_list = response.xpath("//*[@class='item']")
        print(len(game_list))
        for li in game_list:

            url = li.xpath("./div[3]/a/@href").extract_first()
            print(url)
            turn = re.search(r'\d+', url).group()
            self.url_list.append(turn)
            # print(turn)
        next_url = 'http://www.tzuqiu.cc' + '/matches/' + str(turn) + '/report.do'
        print(next_url)
        yield scrapy.Request(next_url, callback=self.parse, headers=self.header)
        print(len(list(set(self.url_list))))
