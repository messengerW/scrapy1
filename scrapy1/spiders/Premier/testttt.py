import scrapy
from scrapy1.items import Test2Item

class ClubsSpider(scrapy.Spider):
    name = 'spider_clubsss'
    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/competitions/1/teamStats.do',]

    def parse(self, response):

        # 四个按钮分别对应四个系列属性(概况、进攻、防守、组织)，先获取到每个系列属性的 20 个 tr...
        clubs_summary = response.xpath("//*[@id='seasonSummary']/tbody/tr")     # -----概况
        clubs_offensive = response.xpath("//*[@id='seasonOffensive']/tbody/tr") # -----进攻
        clubs_defensive = response.xpath("//*[@id='seasonDefensive']/tbody/tr")  # -----防守
        clubs_pass = response.xpath("//*[@id='seasonPass']/tbody/tr")           # -----组织

        for elem1,elem2,elem3,elem4 in zip(clubs_summary,clubs_defensive,clubs_offensive,clubs_pass):
            clubs_item = Test2Item()
            ############################################## 概况
            # 俱乐部名
            clubs_item['name'] = elem1.xpath("./td[2]/a/text()").extract_first()
            # 射门数
            # clubs_item['shoot_total'] = elem1.xpath("./td[3]/text()").extract_first()
            # 控球率
            # clubs_item['possession'] = elem1.xpath("./td[5]/text()").extract_first()
            # 传球成功率
            clubs_item['pass_completed_rate'] = elem1.xpath("./td[6]/text()").extract_first()
            # 绝佳机会
            # clubs_item['great_opportunity'] = elem1.xpath("./td[7]/text()").extract_first()
            # 争顶成功
            clubs_item['flying_header'] = elem1.xpath("./td[8]/text()").extract_first()
            # 评分
            clubs_item['mark'] = elem1.xpath("./td[9]/text()").extract_first()

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
