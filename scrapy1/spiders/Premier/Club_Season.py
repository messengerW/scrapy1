import scrapy
from scrapy1.items import ClubItem

class ClubSeasonSpider(scrapy.Spider):
    name = 'spider_clubs'
    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/competitions/1/teamStats.do',]

    def parse(self, response):

        # 四个按钮分别对应四个系列属性(概况、进攻、防守、组织)，先获取到每个系列属性的 20 个 tr...
        clubs_summary = response.xpath("//*[@id='seasonSummary']/tbody/tr")     # -----概况
        clubs_offensive = response.xpath("//*[@id='seasonOffensive']/tbody/tr") # -----进攻
        clubs_defensive = response.xpath("//*[@id='seasonDefensive']/tbody/tr")  # -----防守
        clubs_pass = response.xpath("//*[@id='seasonPass']/tbody/tr")           # -----组织

        for elem1,elem2,elem3,elem4 in zip(clubs_summary,clubs_offensive,clubs_defensive,clubs_pass):
            clubs_item = ClubItem()
            ############################################## 概况
            # 排名
            clubs_item['a_no'] = elem1.xpath("./td[1]/text()").extract_first()
            # 俱乐部名
            clubs_item['b_name'] = elem1.xpath("./td[2]/a/text()").extract_first()
            # 射门数
            # clubs_item['shoot_total'] = elem1.xpath("./td[3]/text()").extract_first()
            # 控球率
            # clubs_item['possession'] = elem1.xpath("./td[5]/text()").extract_first()
            # 传球成功率
            clubs_item['c_pass_completed_rate'] = elem1.xpath("./td[6]/text()").extract_first()
            # 绝佳机会
            # clubs_item['great_opportunity'] = elem1.xpath("./td[7]/text()").extract_first()
            # 争顶成功
            clubs_item['d_flying_header'] = elem1.xpath("./td[8]/text()").extract_first()
            # 评分
            clubs_item['e_mark'] = elem1.xpath("./td[9]/text()").extract_first()

            ############################################# 进攻
            # 进球
            clubs_item['f_goals'] = elem2.xpath("./td[3]/text()").extract_first()
            # 射门数
            clubs_item['g_shoot_total'] = elem2.xpath("./td[4]/text()").extract_first()
            # 射正数
            clubs_item['h_shoot_on_target'] = elem2.xpath("./td[5]/text()").extract_first()
            # 绝佳机会
            clubs_item['i_great_opportunity'] = elem2.xpath("./td[6]/text()").extract_first()
            # 机会把握率
            clubs_item['j_seize_the_opportunity'] = elem2.xpath("./td[7]/text()").extract_first()
            # 过人
            clubs_item['k_dribble'] = elem2.xpath("./td[8]/text()").extract_first()
            # 被侵犯
            clubs_item['l_violated'] = elem2.xpath("./td[9]/text()").extract_first()
            # 越位
            clubs_item['m_offside'] = elem2.xpath("./td[10]/text()").extract_first()

            ############################################# 防守
            # 失球
            clubs_item['n_fumble'] = elem3.xpath("./td[3]/text()").extract_first()
            # 被射门
            clubs_item['o_be_shoot'] = elem3.xpath("./td[4]/text()").extract_first()
            # 抢断
            clubs_item['p_intercept'] = elem3.xpath("./td[5]/text()").extract_first()
            # 解围
            clubs_item['q_clearance_kick'] = elem3.xpath("./td[7]/text()").extract_first()
            # 犯规
            clubs_item['r_foul'] = elem3.xpath("./td[9]/text()").extract_first()
            # 致命失误
            clubs_item['s_critical_miss'] = elem3.xpath("./td[10]/text()").extract_first()

            #####################################33### 组织
            # 助攻
            clubs_item['t_assisting'] = elem4.xpath("./td[3]/text()").extract_first()
            # 关键传球
            clubs_item['u_key_pass'] = elem4.xpath("./td[4]/text()").extract_first()
            # 控球率
            clubs_item['v_possession'] = elem4.xpath("./td[5]/text()").extract_first()
            # 传球数
            clubs_item['w_pass_total'] = elem4.xpath("./td[6]/text()").extract_first()
            # PS
            clubs_item['x_PS'] = elem4.xpath("./td[7]/text()").extract_first()
            # FTPS
            clubs_item['y_FTPS'] = elem4.xpath("./td[8]/text()").extract_first()

            yield clubs_item
