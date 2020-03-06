"""
    File   : 1617_urls.py
    Author : msw
    Date   : 2020-03-03 21:09
    Ps     : 这是比赛报告页面地址的模板：http://www.tzuqiu.cc/matches/id/report.do
            id: 16/17赛季 1~380
                17/18赛季 5611~5990
                18/19赛季
"""
import re
import scrapy
from fake_useragent import UserAgent

class urls(scrapy.Spider):
    name = 'spider_url'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/matches/1/report.do']

    header = {
        'User-Agent': UserAgent().random,
    }

    url_list = []

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], headers=self.header)

    def parse(self, response):
        game_list = response.xpath("//*[@class='item']")
        # print(len(game_list))
        for li in game_list:
            # 获取比赛报告的 url
            url = li.xpath("./div[3]/a/@href").extract_first()
            # print(url)
            # 取出 url 中的数字，即 id
            turn = re.search(r'\d+', url).group()
            # 加入 url 列表
            self.url_list.append(turn)

        # 检查去重后的列表大小是否等于 380
        print(self.url_list, len(list(set(self.url_list))))

        # 取出列表中最后一个 url 作为下一个爬取网址
        next_url = 'http://www.tzuqiu.cc' + '/matches/' + str(turn) + '/report.do'
        # print(next_url)
        yield scrapy.Request(next_url, callback=self.parse, headers=self.header)