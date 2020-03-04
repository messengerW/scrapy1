"""
    File   : bbs.py
    Author : msw
    Date   : 2020-03-02 15:28
    Ps     : ...
    
"""

import re
import scrapy
from scrapy1.items import MaoItem
from fake_useragent import UserAgent

class Hupubbs(scrapy.Spider):
    name = 'spider3'

    allowed_domains = ['bbs.hupu.com']

    start_urls = ['https://bbs.hupu.com/32727977.html']

    header = {
        'User-Agent': UserAgent().random,
        'Cookie':'_dacevid3=99b32338.c3b4.aa95.f996.8fba77d7cddc; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f1449ff1b17a-05000e0a039f99-6701434-921600-16f1449ff1c589%22%2C%22%24device_id%22%3A%2216f1449ff1b17a-05000e0a039f99-6701434-921600-16f1449ff1c589%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _HUPUSSOID=95ff3c94-0462-4da4-8f6c-16eff42434a3; AUM=dglnDpd4SfNcmYuIkFJjjmF3jN5nt-yqlWtWpTno5j7lw; acw_tc=781bad2815831335488584649e20d533b7abeec661712d3f53c87c2f688d7c; _cnzz_CV30020080=buzi_cookie%7C99b32338.c3b4.aa95.f996.8fba77d7cddc%7C-1; _CLT=868ae16f150cf61ab926af24b4aa60be; u=20499914|55So5oi3MDI5NjA3NzU4NQ==|fb51|d9b364dde8d2d7784975cf4128bc8c7e|e8d2d7784975cf41|5L2g6KGM5L2g5YCS5LiK5ZWK; us=e940bcad2f556ffe6ee167798c5adc238e460430421d774a07413bb4fa4d7e9f34fd387fc4bd6f60e05525c82643d463a8549a9cd5fbe02b7217666bb78fed0d; Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1580550825,1580565852,1583133548,1583133593; ua=105542241; PHPSESSID=51786139cfb1d156440eb9844349e6e2; lastvisit=361%091583133982%09%2Fajax%2FgetNewReply.ajax.php%3Ftid%3D32733013%26pid%3D23599%26lou%3D13%26_%3D1583133980891; __dacevst=f3d486cd.85dcafb9|1583136266502; Hm_lpvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1583134467; _fmdata=eyZJLviJHoYkPZPj%2FiJZ3vzyf1bZHj%2BLUscYti37hYsNM7LWxutR5A3u281ykRJsskCevmjcTVGz885atmEGeD51B3Jsil1ipHRdlNK66xQ%3D'    }


    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], headers=self.header)

    def parse(self, response):
        li_list = response.xpath("//*[@id='readfloor']/div")

        for li in li_list:
            topic = MaoItem()

            topic['time'] = li.xpath("./div[2]").extract_first()

            yield topic

        for i in range(2, 10):
            left = re.search(r'.*\d+', self.start_urls[0]).group()
            right = "-" + str(i) + ".html"
            next_page = left + right
            yield scrapy.Request(next_page, callback=self.parse,
                                 headers=self.header)

