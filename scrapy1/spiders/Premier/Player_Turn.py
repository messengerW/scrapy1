import re
import json
import scrapy
from scrapy import Request
from scrapy1.items import Test1Item


class DDDSpider(scrapy.Spider):
    name = 'spider_b'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.tzuqiu.cc',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Cookie': '_ga=GA1.2.310854451.1568169977; _gid=GA1.2.577790814.1568169977; Hm_lvt_b83b828716a7230e966a4555be5f6151=1568169976,1568191239,1568212141; _gat_gtag_UA_121641862_1=1; JSESSIONID=7EDD8EE6D36B4163C63B3F2EBCF742CD; Hm_lpvt_b83b828716a7230e966a4555be5f6151=1568606800',
    }

    def start_requests(self):
        url = 'http://www.tzuqiu.cc/playerStatistics/querysStat.json?draw=2&columns%5B0%5D%5Bdata%5D=id&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=playerFormat&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=appsFormat&columns%5B2%5D%5Bname%5D=psp.appsCP&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=minsFormat&columns%5B3%5D%5Bname%5D=psp.minsCP&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=goalsFormat&columns%5B4%5D%5Bname%5D=psp.goalsCP&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=assistsFormat&columns%5B5%5D%5Bname%5D=psp.assistsCP&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=cardsFormat&columns%5B6%5D%5Bname%5D=psp.cardsCP&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=passSuccFormat&columns%5B7%5D%5Bname%5D=psp.passSuccCP&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=bigChanceCreatedFormat&columns%5B8%5D%5Bname%5D=psp.bigChanceCreatedCP&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=aerialWonFormat&columns%5B9%5D%5Bname%5D=psp.aerialWonCP&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=mansFormat&columns%5B10%5D%5Bname%5D=psp.mansCP&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=rateFormat&columns%5B11%5D%5Bname%5D=psp.rateCP&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&extra_param%5BcompetitionId%5D=1&extra_param%5Bseason%5D=19%2F20&extra_param%5BorderCdnReq%5D=true&_=1568614570999'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        datas = json.loads(response.body)
        item = Test1Item()

        draw = 2
        start = 0
        _ = 1568614570999
        url1 = 'http://www.tzuqiu.cc/playerStatistics/querysStat.json?draw='
        url2 = '&columns%5B0%5D%5Bdata%5D=id&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=playerFormat&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=appsFormat&columns%5B2%5D%5Bname%5D=psp.appsCP&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=minsFormat&columns%5B3%5D%5Bname%5D=psp.minsCP&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=goalsFormat&columns%5B4%5D%5Bname%5D=psp.goalsCP&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=assistsFormat&columns%5B5%5D%5Bname%5D=psp.assistsCP&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=cardsFormat&columns%5B6%5D%5Bname%5D=psp.cardsCP&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=passSuccFormat&columns%5B7%5D%5Bname%5D=psp.passSuccCP&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=bigChanceCreatedFormat&columns%5B8%5D%5Bname%5D=psp.bigChanceCreatedCP&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=aerialWonFormat&columns%5B9%5D%5Bname%5D=psp.aerialWonCP&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=mansFormat&columns%5B10%5D%5Bname%5D=psp.mansCP&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=rateFormat&columns%5B11%5D%5Bname%5D=psp.rateCP&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&start='
        url3 = '&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&extra_param%5BcompetitionId%5D=1&extra_param%5Bseason%5D=19%2F20&extra_param%5BorderCdnReq%5D=true&_='

        if datas['data']:
            for data in datas['data']:
                item['no'] = data['id']
                item['name'] = data['playerName']
                item['club'] = data['teamName']
                item['age'] = data['age']
                yield item

            # # 如果datas存在数据则对下一页进行采集
            # page_num = re.search(r'start=(\d+)', response.url).group(1)
            # page_num = 'start=' + str(int(page_num) + 20)
            # next_url = re.sub(r'start=\d+', page_num, response.url)
            # yield Request(next_url, headers=self.headers)

            draw += 1
            start += 10
            _ += 1
            nexturl = url1 + str(draw) + url2 + str(start) + url3 + str(_)
            print("||||||||||||||||| nexturl:"+nexturl)
            print("||||||||||||||||||||||respon.url:"+response.url)
            yield Request(nexturl, headers=self.headers)
