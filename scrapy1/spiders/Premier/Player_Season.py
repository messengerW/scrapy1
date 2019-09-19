import re
import json
import time
import scrapy
from scrapy import Request
from scrapy1.items import Test1Item


class DDDSpider(scrapy.Spider):
    name = 'spider_bbb'

    def start_requests(self):
        url = 'http://www.tzuqiu.cc/playerStatistics/querysStat.json?draw=1&columns%5B0%5D%5Bdata%5D=id&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=playerFormat&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=appsFormat&columns%5B2%5D%5Bname%5D=psp.appsCP&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=minsFormat&columns%5B3%5D%5Bname%5D=psp.minsCP&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=goalsFormat&columns%5B4%5D%5Bname%5D=psp.goalsCP&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=assistsFormat&columns%5B5%5D%5Bname%5D=psp.assistsCP&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=cardsFormat&columns%5B6%5D%5Bname%5D=psp.cardsCP&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=passSuccFormat&columns%5B7%5D%5Bname%5D=psp.passSuccCP&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=bigChanceCreatedFormat&columns%5B8%5D%5Bname%5D=psp.bigChanceCreatedCP&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=aerialWonFormat&columns%5B9%5D%5Bname%5D=psp.aerialWonCP&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=mansFormat&columns%5B10%5D%5Bname%5D=psp.mansCP&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=rateFormat&columns%5B11%5D%5Bname%5D=psp.rateCP&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&extra_param%5BcompetitionId%5D=1&extra_param%5Bseason%5D=19%2F20&extra_param%5BorderCdnReq%5D=true&_=1568866686557'
        yield Request(url)

    def parse(self, response):
        datas = json.loads(response.body)
        item = Test1Item()
        time.sleep(1)

        if datas['data']:

            for data in datas['data']:
                item['no'] = data['id']
                item['name'] = data['playerName']
                item['club'] = data['teamName']
                item['age'] = data['age']
                yield item

            _draw = re.search(r"draw=(\d+)", response.url).group(1)
            _start = re.search(r"start=(\d+)", response.url).group(1)
            _value = re.search(r"&_=(\d+)", response.url).group(1)

            _draw = 'draw=' + str(int(_draw) + 1)
            _start = 'start=' + str(int(_start) + 10)
            _value = '_=' + str(int(_value) + 1)
            nexturl = re.sub(r"draw=(\d+)", _draw, response.url)
            nexturl = re.sub(r"start=(\d+)", _start, nexturl)
            nexturl = re.sub(r"_=(\d+)", _value, nexturl)
            yield Request(nexturl)