"""
    File   : History_Match_Info.py
    Author : msw
    Date   : 2020-03-04 22:00
    Ps     : http://www.tzuqiu.cc/matches/13966/report.do 这个是比赛信息页面,id 分布规律如下:
            1 - 380     是16-17赛季全部的 380 场比赛信息
            5611 - 5990     17/18赛季
            52439 - 52818   18/19赛季
            11306 - 11685	15/16赛季
            11686 - 12065	14/15赛季
            12066 - 12445	13/14赛季
            12446 - 12825	12/13赛季
            12826 - 13205	11/12赛季
            13206 - 13585	10/11赛季
            13586 - 13965	09/10赛季
    
"""
import re
import time
import scrapy
from scrapy1.items import GameItem
from fake_useragent import UserAgent

class MatchInfo(scrapy.Spider):

    name = 'spider_match'
    allowed_domains = ['tzuqiu.cc']

    header = {
        'User-Agent': UserAgent().random,
    }

    def start_requests(self):
        for i in range(12446, 12826):
            time.sleep(1)
            url = 'http://www.tzuqiu.cc' + '/matches/' + str(i) + '/report.do'
            yield scrapy.Request(url, headers=self.header)

    def parse(self, response):
        game_item = GameItem()

        # 轮次
        round = response.xpath("//td[@class='stat-box']/text()").extract_first()
        if round:
            # strip()函数移除字符串头尾指定的字符（默认为空格或换行符），ps：对中间部分无效
            round = round.strip()
        else:
            round = ' '
        game_item['round'] = round

        # 比赛时间
        # 下面这句话有个坑，这个 tbody 有问题，加了就是空属性，不知道为什么。
        # //td[@class='match-info']//tbody/tr[5]/td[2]/text() 就会错，去掉tbody就没问题
        date_str = response.xpath("//td[@class='match-info']//tr[5]/td[2]/text()").extract_first()
        if date_str:
            date_str = ''.join(date_str.split())
            date_list = list(date_str)
            date_list.insert(10, ' ')
            date = ''.join(date_list)
        else:
            date = ' '
        game_item['date'] = date

        # 比分
        game_item['score'] = response.xpath("//td[@class='result']/text()").extract_first()

        # 主队客队以 1/2 区分
        game_item['team1'] = response.xpath("/html/body/div[3]/div[2]/div[1]/div[1]/table/tr[1]/td[1]/a/text()").extract_first()
        game_item['team2'] = response.xpath("/html/body/div[3]/div[2]/div[1]/div[1]/table/tr[1]/td[3]/a/text()").extract_first()

        # 主队进球数
        goals1 = response.xpath(
            "//*[@id='shotsTab']/div[2]/div/div[3]/span/span[2]/span/text()").extract_first()
        if goals1:
            goals1 = goals1.strip()
        else:
            goals1 = ''
        game_item['goals1'] = goals1
        # 客队进球数
        goals2 = response.xpath(
            "//*[@id='shotsTab']/div[2]/div/div[3]/span/span[4]/span/text()").extract_first()
        if goals2:
            goals2 = goals2.strip()
        else:
            goals2 = ''
        game_item['goals2'] = goals2

        # 主队控球率
        possession1 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[2]/div[2]/span[1]/span[2]/span/text()").extract_first()
        if possession1:
            possession1 = possession1.strip()
        else:
            possession1 = ' '
        game_item['possession1'] = possession1
        # 客队控球率
        possession2 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[2]/div[2]/span[1]/span[3]/span/text()").extract_first()
        if possession2:
            possession2 = possession2.strip()
        else:
            possession2 = ' '
        game_item['possession2'] = possession2

        # 对抗成功率
        confrontation_win_rate1 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[4]/span[1]/span/text()").extract_first()
        if confrontation_win_rate1:
            confrontation_win_rate1 = confrontation_win_rate1.strip()
        else:
            confrontation_win_rate1 = ' '
        game_item['confrontation_win_rate1'] = confrontation_win_rate1
        # 对抗成功率
        confrontation_win_rate2 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[4]/span[3]/span/text()").extract_first()
        if confrontation_win_rate2:
            confrontation_win_rate2 = confrontation_win_rate2.strip()
        else:
            confrontation_win_rate2 = ' '
        game_item['confrontation_win_rate2'] = confrontation_win_rate2

        # 过人
        dribble1 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[5]/span[1]/span/text()").extract_first()
        if dribble1:
            dribble1 = dribble1.strip()
        else:
            dribble1 = ' '
        game_item['dribble1'] = dribble1
        # 过人
        dribble2 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[5]/span[3]/span/text()").extract_first()
        if dribble2:
            dribble2 = dribble2.strip()
        else:
            dribble2 = ' '
        game_item['dribble2'] = dribble2

        # 抢断
        intercept1 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[6]/span[1]/span/text()").extract_first()
        if intercept1:
            intercept1 = intercept1.strip()
        else:
            intercept1 = ' '
        game_item['intercept1'] = intercept1
        # 抢断
        intercept2 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[6]/span[3]/span/text()").extract_first()
        if intercept2:
            intercept2 = intercept2.strip()
        else:
            intercept2 = ' '
        game_item['intercept2'] = intercept2

        # 球队评分
        mark = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[7]/span[1]/span/text()").extract_first()
        if mark:
            mark = mark.strip()
        else:
            mark = ' '
        game_item['mark1'] = mark
        # 球队评分
        mark2 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[7]/span[3]/span/text()").extract_first()
        if mark2:
            mark2 = mark2.strip()
        else:
            mark2 = ' '
        game_item['mark2'] = mark2

        # 射门数
        shoot_total = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[1]/span[1]/span/text()").extract_first()
        if shoot_total:
            shoot_total = shoot_total.strip()
        else:
            shoot_total = ' '
        game_item['shoot_total1'] = shoot_total
        # 射门数
        shoot_total2 = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[1]/span[3]/span/text()").extract_first()
        if shoot_total2:
            shoot_total2 = shoot_total2.strip()
        else:
            shoot_total2 = ' '
        game_item['shoot_total2'] = shoot_total2

        # 阵地战
        shoot_positional = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[2]/span[1]/span/text()").extract_first()
        if shoot_positional:
            shoot_positional = shoot_positional.strip()
        else:
            shoot_positional = ' '
        game_item['shoot_positional1'] = shoot_positional
        # 阵地战
        shoot_positional2 = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[2]/span[3]/span/text()").extract_first()
        if shoot_positional2:
            shoot_positional2 = shoot_positional2.strip()
        else:
            shoot_positional2 = ' '
        game_item['shoot_positional2'] = shoot_positional2

        # 定位球
        shoot_placekick = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[3]/span[1]/span/text()").extract_first()
        if shoot_placekick:
            shoot_placekick = shoot_placekick.strip()
        else:
            shoot_placekick = ' '
        game_item['shoot_placekick1'] = shoot_placekick
        # 定位球
        shoot_placekick2 = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[3]/span[3]/span/text()").extract_first()
        if shoot_placekick2:
            shoot_placekick2 = shoot_placekick2.strip()
        else:
            shoot_placekick2 = ' '
        game_item['shoot_placekick2'] = shoot_placekick2

        # 反击
        shoot_counterattack = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[4]/span[1]/span/text()").extract_first()
        if shoot_counterattack:
            shoot_counterattack = shoot_counterattack.strip()
        else:
            shoot_counterattack = ' '
        game_item['shoot_counterattack1'] = shoot_counterattack
        # 反击
        shoot_counterattack2 = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[4]/span[3]/span/text()").extract_first()
        if shoot_counterattack2:
            shoot_counterattack2 = shoot_counterattack2.strip()
        else:
            shoot_counterattack2 = ' '
        game_item['shoot_counterattack2'] = shoot_counterattack2

        # 点球
        penalty = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[5]/span[1]/span/text()").extract_first()
        if penalty:
            penalty = penalty.strip()
        else:
            penalty = ' '
        game_item['penalty1'] = penalty
        # 点球
        penalty2 = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[5]/span[3]/span/text()").extract_first()
        if penalty2:
            penalty2 = penalty2.strip()
        else:
            penalty2 = ' '
        game_item['penalty2'] = penalty2

        # 乌龙球
        own_goal = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[6]/span[1]/span/text()").extract_first()
        if own_goal:
            own_goal = own_goal.strip()
        else:
            own_goal = ' '
        game_item['own_goal1'] = own_goal
        # 乌龙球
        own_goal2 = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[6]/span[3]/span/text()").extract_first()
        if own_goal2:
            own_goal2 = own_goal2.strip()
        else:
            own_goal2 = ' '
        game_item['own_goal2'] = own_goal2

        # 射正数
        shoot_on_target = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[2]/span[1]/span/text()").extract_first()
        if shoot_on_target:
            shoot_on_target = shoot_on_target.strip()
        else:
            shoot_on_target = ' '
        game_item['shoot_on_target1'] = shoot_on_target
        # 射正数
        shoot_on_target2 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[2]/span[3]/span/text()").extract_first()
        if shoot_on_target2:
            shoot_on_target2 = shoot_on_target2.strip()
        else:
            shoot_on_target2 = ' '
        game_item['shoot_on_target2'] = shoot_on_target2

        # 传球数
        pass_total = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[1]/span[1]/span/text()").extract_first()
        if pass_total:
            pass_total = pass_total.strip()
        else:
            pass_total = ' '
        game_item['pass_total1'] = pass_total
        # 传球数
        pass_total2 = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[1]/span[3]/span/text()").extract_first()
        if pass_total2:
            pass_total2 = pass_total2.strip()
        else:
            pass_total2 = ' '
        game_item['pass_total2'] = pass_total2

        # 短传
        pass_short = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[2]/span[1]/span/text()").extract_first()
        if pass_short:
            pass_short = pass_short.strip()
        else:
            pass_short = ' '
        game_item['pass_short1'] = pass_short
        # 短传
        pass_short2 = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[2]/span[3]/span/text()").extract_first()
        if pass_short2:
            pass_short2 = pass_short2.strip()
        else:
            pass_short2 = ' '
        game_item['pass_short2'] = pass_short2

        # 长传
        pass_long = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[3]/span[1]/span/text()").extract_first()
        if pass_long:
            pass_long = pass_long.strip()
        else:
            pass_long = ' '
        game_item['pass_long1'] = pass_long
        # 长传
        pass_long2 = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[3]/span[3]/span/text()").extract_first()
        if pass_long2:
            pass_long2 = pass_long2.strip()
        else:
            pass_long2 = ' '
        game_item['pass_long2'] = pass_long2

        # 传中
        pass_center = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[4]/span[1]/span/text()").extract_first()
        if pass_center:
            pass_center = pass_center.strip()
        else:
            pass_center = ' '
        game_item['pass_center1'] = pass_center
        # 传中
        pass_center2 = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[4]/span[3]/span/text()").extract_first()
        if pass_center2:
            pass_center2 = pass_center2.strip()
        else:
            pass_center2 = ' '
        game_item['pass_center2'] = pass_center2

        # 直塞
        pass_through = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[5]/span[1]/span/text()").extract_first()
        if pass_through:
            pass_through = pass_through.strip()
        else:
            pass_through = ' '
        game_item['pass_through1'] = pass_through
        # 直塞
        pass_through2 = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[5]/span[3]/span/text()").extract_first()
        if pass_through2:
            pass_through2 = pass_through2.strip()
        else:
            pass_through2 = ' '
        game_item['pass_through2'] = pass_through2

        # 传球成功率
        pass_completed_rate = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[3]/span[1]/span/text()").extract_first()
        if pass_completed_rate:
            pass_completed_rate = pass_completed_rate.strip()
        else:
            pass_completed_rate = ' '
        game_item['pass_completed_rate1'] = pass_completed_rate
        # 传球成功率
        pass_completed_rate2 = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[3]/span[3]/span/text()").extract_first()
        if pass_completed_rate2:
            pass_completed_rate2 = pass_completed_rate2.strip()
        else:
            pass_completed_rate2 = ' '
        game_item['pass_completed_rate2'] = pass_completed_rate2

        # 积分
        game_item['points'] = ''

        time.sleep(3)
        yield game_item