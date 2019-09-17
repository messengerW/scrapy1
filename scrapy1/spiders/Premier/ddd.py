import re
import json
import scrapy
from scrapy import Request
from scrapy1.items import Test1Item

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
        url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        datas = json.loads(response.body)
        item = Test1Item()
        if datas:
            for data in datas:
                item['no'] = data['rank']
                item['name'] = data['title']
                item['club'] = data['score']
                item['age'] = data['vote_count']
                yield item

            # 如果datas存在数据则对下一页进行采集
            print("===>>>>>>"+response.url)
            page_num = re.search(r'start=(\d+)', response.url).group(1)
            page_num = 'start=' + str(int(page_num) + 20)
            next_url = re.sub(r'start=\d+', page_num, response.url)
            yield Request(next_url, headers=self.headers)