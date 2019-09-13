import scrapy
from scrapy1.items import Test2Item

class ClubsSpider(scrapy.Spider):
    name = 'spider_club3'
    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/competitions/1/teamStats.do',]

    def parse(self, response):

        # 四个按钮分别对应四个系列属性(概况、进攻、防守、组织)，先获取到每个系列属性的 20 个 tr
        clubs_summary = response.xpath("//*[@id='seasonSummary']/tbody/tr")     # -----概况
        clubs_offensive = response.xpath("//*[@id='seasonOffensive']/tbody/tr") # -----进攻
        clubs_defensive = response.xpath("//*[@id='seasonDefensive']/tbody/tr")  # -----防守
        clubs_pass = response.xpath("//*[@id='seasonPass']/tbody/tr")           # -----组织

        for elem3 in clubs_defensive:
            clubs_item = Test2Item()
            ############################################# 防守
            # 失球
            clubs_item['fumble'] = elem3.xpath("./td[3]/text()").extract_first()
            # 被射门
            clubs_item['be_shoot'] = elem3.xpath("./td[4]/text()").extract_first()
            # 抢断
            clubs_item['intercept'] = elem3.xpath("./td[5]/text()").extract_first()
            # 解围
            clubs_item['clearance_kick'] = elem3.xpath("./td[7]/text()").extract_first()
            # 犯规
            clubs_item['foul'] = elem3.xpath("./td[9]/text()").extract_first()
            # 致命失误
            clubs_item['critical_miss'] = elem3.xpath("./td[10]/text()").extract_first()
            yield clubs_item
