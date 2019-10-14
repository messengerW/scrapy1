import re
import json
import scrapy
from scrapy import Request
from scrapy1.items import PlayerTurnItem

class DDDSpider(scrapy.Spider):
    name = 'spider_ddd'

    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = PlayerTurnItem()
        datas = json.loads(response.body)
        if datas:
            for data in datas:
                item['no'] = data['rank']
                item['name'] = data['title']
                yield item

            start = re.search(r"start=(\d+)", response.url).group(1)
            start = 'start=' + str(int(start) + 20)
            nexturl = re.sub(r"start=(\d+)", start, response.url)

            print("start:%s\nnexturl:%s" % (start, nexturl))
            yield Request(url=nexturl,headers=self.headers)