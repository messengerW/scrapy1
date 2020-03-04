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

    start_urls = ['https://bbs.hupu.com/bxj-11']

    header = {
        'User-Agent': UserAgent().random,
        'Cookie': '_dacevid3=99b32338.c3b4.aa95.f996.8fba77d7cddc; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f1449ff1b17a-05000e0a039f99-6701434-921600-16f1449ff1c589%22%2C%22%24device_id%22%3A%2216f1449ff1b17a-05000e0a039f99-6701434-921600-16f1449ff1c589%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _HUPUSSOID=95ff3c94-0462-4da4-8f6c-16eff42434a3; acw_tc=781bad2415803806923592126e0987732c2780f1e7319c5ff9acd1340621b0; _cnzz_CV30020080=buzi_cookie%7C99b32338.c3b4.aa95.f996.8fba77d7cddc%7C-1; PHPSESSID=5b630582a0eb7d716eea2ab35e253b25; _fmdata=eyZJLviJHoYkPZPj%2FiJZ3vzyf1bZHj%2BLUscYti37hYsNM7LWxutR5A3u281ykRJsQ9bjuI%2FyK320GYQ%2B5geuHnbFc%2B34DX8HqBmxSKaSozM%3D; _CLT=868ae16f150cf61ab926af24b4aa60be; u=20499914|55So5oi3MDI5NjA3NzU4NQ==|fb51|d9b364dde8d2d7784975cf4128bc8c7e|e8d2d7784975cf41|5L2g6KGM5L2g5YCS5LiK5ZWK; Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1580478507,1580478516,1580543763,1580550825; us=; ua=105370945; Hm_lpvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1580564185; __dacevst=bd2fc241.bb349233|1580565994225'
    }

    def start_requests(self):
        cookies = '_dacevid3=99b32338.c3b4.aa95.f996.8fba77d7cddc; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f1449ff1b17a-05000e0a039f99-6701434-921600-16f1449ff1c589%22%2C%22%24device_id%22%3A%2216f1449ff1b17a-05000e0a039f99-6701434-921600-16f1449ff1c589%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _HUPUSSOID=95ff3c94-0462-4da4-8f6c-16eff42434a3; acw_tc=781bad2415803806923592126e0987732c2780f1e7319c5ff9acd1340621b0; _cnzz_CV30020080=buzi_cookie%7C99b32338.c3b4.aa95.f996.8fba77d7cddc%7C-1; PHPSESSID=5b630582a0eb7d716eea2ab35e253b25; _fmdata=eyZJLviJHoYkPZPj%2FiJZ3vzyf1bZHj%2BLUscYti37hYsNM7LWxutR5A3u281ykRJsQ9bjuI%2FyK320GYQ%2B5geuHnbFc%2B34DX8HqBmxSKaSozM%3D; _CLT=868ae16f150cf61ab926af24b4aa60be; u=20499914|55So5oi3MDI5NjA3NzU4NQ==|fb51|d9b364dde8d2d7784975cf4128bc8c7e|e8d2d7784975cf41|5L2g6KGM5L2g5YCS5LiK5ZWK; Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1580478507,1580478516,1580543763,1580550825; us=; ua=105370945; Hm_lpvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1580564185; __dacevst=bd2fc241.bb349233|1580565994225'
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
        yield scrapy.Request(self.start_urls[0], cookies=cookies)

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

        # for i in range(30,41):
        #     time.sleep(1)
        #     next_url = self.start_urls[0] + "-" + str(i)
        #     # print(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse, headers=self.header)
