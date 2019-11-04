"""
    File   : station.py
    Author : msw
    Date   : 2019/11/4 15:47
    Ps     : 爬取杭州市公交站点
    
"""
import scrapy
from scrapy import Request
from scrapy1.items import StationItem

class StationSpider(scrapy.Spider):
    name = 'spider_station'


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'hangzhou.8684.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://hangzhou.8684.cn/so.php?q=&k=p'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        # 获取到所有的站点标签 <a></a>
        tag_list = response.xpath("//div[@class='list clearfix']/a")

        for _tag in tag_list:
            station_item = StationItem()

            station_item['station'] = _tag.xpath("./text()").extract_first()

            yield station_item

