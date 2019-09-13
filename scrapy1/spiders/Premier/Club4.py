import scrapy
from scrapy1.items import Test2Item

class ClubsSpider(scrapy.Spider):
    name = 'spider_club4'
    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/competitions/1/teamStats.do',]

    def parse(self, response):

        # 四个按钮分别对应四个系列属性(概况、进攻、防守、组织)，先获取到每个系列属性的 20 个 tr
        clubs_summary = response.xpath("//*[@id='seasonSummary']/tbody/tr")     # -----概况
        clubs_offensive = response.xpath("//*[@id='seasonOffensive']/tbody/tr") # -----进攻
        clubs_defensive = response.xpath("/*[@id='seasonDefensive']/tbody/tr")  # -----防守
        clubs_pass = response.xpath("//*[@id='seasonPass']/tbody/tr")           # -----组织

        for elem4 in clubs_pass:
            clubs_item = Test2Item()
            #####################################33### 组织
            # 助攻
            clubs_item['assisting'] = elem4.xpath("./td[3]/text()").extract_first()
            # 关键传球
            clubs_item['key_pass'] = elem4.xpath("./td[4]/text()").extract_first()
            # 控球率
            clubs_item['possession'] = elem4.xpath("./td[5]/text()").extract_first()
            # 传球数
            clubs_item['pass_total'] = elem4.xpath("./td[6]/text()").extract_first()
            # PS
            clubs_item['PS'] = elem4.xpath("./td[7]/text()").extract_first()
            # FTPS
            clubs_item['FTPS'] = elem4.xpath("./td[8]/text()").extract_first()

            yield clubs_item
