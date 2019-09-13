import scrapy
from scrapy1.items import Test2Item

class ClubsSpider(scrapy.Spider):
    name = 'spider_club2'
    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/competitions/1/teamStats.do',]

    def parse(self, response):

        # 四个按钮分别对应四个系列属性(概况、进攻、防守、组织)，先获取到每个系列属性的 20 个 tr
        clubs_summary = response.xpath("//*[@id='seasonSummary']/tbody/tr")     # -----概况
        clubs_offensive = response.xpath("//*[@id='seasonOffensive']/tbody/tr") # -----进攻
        clubs_defensive = response.xpath("/*[@id='seasonDefensive']/tbody/tr")  # -----防守
        clubs_pass = response.xpath("//*[@id='seasonPass']/tbody/tr")           # -----组织

        for elem2 in clubs_offensive:
            clubs_item = Test2Item()
            ############################################# 进攻
            # 进球
            clubs_item['goals'] = elem2.xpath("./td[3]/text()").extract_first()
            # 射门数
            clubs_item['shoot_total'] = elem2.xpath("./td[4]/text()").extract_first()
            # 射正数
            clubs_item['shoot_on_target'] = elem2.xpath("./td[5]/text()").extract_first()
            # 绝佳机会
            clubs_item['great_opportunity'] = elem2.xpath("./td[6]/text()").extract_first()
            # 机会把握率
            clubs_item['seize_the_opportunity'] = elem2.xpath("./td[7]/text()").extract_first()
            # 过人
            clubs_item['dribble'] = elem2.xpath("./td[8]/text()").extract_first()
            # 被侵犯
            clubs_item['violated'] = elem2.xpath("./td[9]/text()").extract_first()
            # 越位
            clubs_item['offside'] = elem2.xpath("./td[10]/text()").extract_first()
            yield clubs_item