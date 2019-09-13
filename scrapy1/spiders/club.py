# 2019.04.26

import scrapy
from scrapy1.items import ClubItem


class ClubSpider(scrapy.Spider):
    name = 'spider_club'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/competitions/1/show.do']

    def parse(self, response):
        club_list = response.xpath("//*[@id='rankTable0']/tbody/tr")
        for i_item in club_list:
            club_item = ClubItem()
            club_item['rank'] = i_item.xpath("./td[1]/span/text()").extract_first()
            club_item['name'] = i_item.xpath(".//td[2]/a/text()").extract_first()
            club_item['turn'] = i_item.xpath(".//td[3]/text()").extract_first()
            club_item['win'] = i_item.xpath(".//td[4]/text()").extract_first()
            club_item['tie'] = i_item.xpath(".//td[5]/text()").extract_first()
            club_item['lose'] = i_item.xpath(".//td[6]/text()").extract_first()
            club_item['goals'] = i_item.xpath(".//td[7]/text()").extract_first()
            club_item['fumble'] = i_item.xpath(".//td[8]/text()").extract_first()
            club_item['delt'] = i_item.xpath(".//td[9]/text()").extract_first()
            club_item['score'] = i_item.xpath(".//td[10]/text()").extract_first()

            yield club_item