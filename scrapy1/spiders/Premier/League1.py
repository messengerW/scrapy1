# 2019.05.20
# 做了点修改，每次手动改网址太麻烦，我本来想写一个爬虫类用来爬网址，然后其它爬虫调用它就可以了，
# 但是试了很多次不行（还是太菜），没办法我就先把爬下来的网址都放到一个excel里面，然后从这个
# excel里面读取，也可以达到效果，不过还是有点麻烦.

# 这个是通用的，geturl那边获取完url后这边就可以直接爬了 : scrapy crawl spider_League -o ×××.×××
# 1 的意思是主队，2是客队

import scrapy
import time
import xlrd
from scrapy1.items import GameItem


class GameSpider(scrapy.Spider):
    name = 'spider_League1'

    allowed_domains = ['tzuqiu.cc']

    start_urls = []

    # 设置文件名和路径
    filepath = 'C:/Users/mushr/Desktop/433/创3/urls.xlsx'
    # 打开 excel
    book = xlrd.open_workbook(filepath)
    # 获取第一个 sheet
    sheet = book.sheets()[0]

    # 获取表的行数、列数
    rows_num = sheet.nrows
    cols_num = sheet.ncols
    # 从第2行（下标1）开始读取
    for i_row in range(1, rows_num):
        url = sheet.row_values(i_row)[0]  # 主场，所以获取excel第1列
        if url:
            # print(url)
            start_urls.append(url)

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

        # 进球
        goals_total = response.xpath(
            "//div[@id='shotsTab']/div[2]/div[1]/div[3]/span[1]/span[2]/span/text()").extract_first()
        if goals_total:
            goals_total = goals_total.strip()
        else:
            goals_total = ' '
        game_item['goals_total'] = goals_total

        # 主队进球数
        game_item['goals_home'] = ''

        # 客队进球数
        game_item['goals_away'] = ''

        # 控球率
        possession = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[2]/div[2]/span[1]/span[2]/span/text()").extract_first()
        if possession:
            possession = possession.strip()
        else:
            possession = ' '
        game_item['possession'] = possession

        # 对抗成功率
        confrontation_win_rate = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[4]/span[1]/span/text()").extract_first()
        if confrontation_win_rate:
            confrontation_win_rate = confrontation_win_rate.strip()
        else:
            confrontation_win_rate = ' '
        game_item['confrontation_win_rate'] = confrontation_win_rate

        # 过人
        dribble = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[5]/span[1]/span/text()").extract_first()
        if dribble:
            dribble = dribble.strip()
        else:
            dribble = ' '
        game_item['dribble'] = dribble

        # 抢断
        intercept = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[6]/span[1]/span/text()").extract_first()
        if intercept:
            intercept = intercept.strip()
        else:
            intercept = ' '
        game_item['intercept'] = intercept

        # 球队评分
        mark = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[7]/span[1]/span/text()").extract_first()
        if mark:
            mark = mark.strip()
        else:
            mark = ' '
        game_item['mark'] = mark

        # 主客场 (手动填写)
        game_item['home_or_away'] = '主'

        # 射门数
        shoot_total = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[1]/span[1]/span/text()").extract_first()
        if shoot_total:
            shoot_total = shoot_total.strip()
        else:
            shoot_total = ' '
        game_item['shoot_total'] = shoot_total

        # 阵地战
        shoot_positional = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[2]/span[1]/span/text()").extract_first()
        if shoot_positional:
            shoot_positional = shoot_positional.strip()
        else:
            shoot_positional = ' '
        game_item['shoot_positional'] = shoot_positional

        # 定位球
        shoot_placekick = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[3]/span[1]/span/text()").extract_first()
        if shoot_placekick:
            shoot_placekick = shoot_placekick.strip()
        else:
            shoot_placekick = ' '
        game_item['shoot_placekick'] = shoot_placekick

        # 反击
        shoot_counterattack = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[4]/span[1]/span/text()").extract_first()
        if shoot_counterattack:
            shoot_counterattack = shoot_counterattack.strip()
        else:
            shoot_counterattack = ' '
        game_item['shoot_counterattack'] = shoot_counterattack

        # 点球
        penalty = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[5]/span[1]/span/text()").extract_first()
        if penalty:
            penalty = penalty.strip()
        else:
            penalty = ' '
        game_item['penalty'] = penalty

        # 乌龙球
        own_goal = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[6]/span[1]/span/text()").extract_first()
        if own_goal:
            own_goal = own_goal.strip()
        else:
            own_goal = ' '
        game_item['own_goal'] = own_goal

        # 射正数
        shoot_on_target = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[2]/span[1]/span/text()").extract_first()
        if shoot_on_target:
            shoot_on_target = shoot_on_target.strip()
        else:
            shoot_on_target = ' '
        game_item['shoot_on_target'] = shoot_on_target

        # 传球数
        pass_total = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[1]/span[1]/span/text()").extract_first()
        if pass_total:
            pass_total = pass_total.strip()
        else:
            pass_total = ' '
        game_item['pass_total'] = pass_total

        # 短传
        pass_short = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[2]/span[1]/span/text()").extract_first()
        if pass_short:
            pass_short = pass_short.strip()
        else:
            pass_short = ' '
        game_item['pass_short'] = pass_short

        # 长传
        pass_long = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[3]/span[1]/span/text()").extract_first()
        if pass_long:
            pass_long = pass_long.strip()
        else:
            pass_long = ' '
        game_item['pass_long'] = pass_long

        # 传中
        pass_center = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[4]/span[1]/span/text()").extract_first()
        if pass_center:
            pass_center = pass_center.strip()
        else:
            pass_center = ' '
        game_item['pass_center'] = pass_center

        # 直塞
        pass_through = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[5]/span[1]/span/text()").extract_first()
        if pass_through:
            pass_through = pass_through.strip()
        else:
            pass_through = ' '
        game_item['pass_through'] = pass_through

        # 传球成功率
        pass_completed_rate = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[3]/span[1]/span/text()").extract_first()
        if pass_completed_rate:
            pass_completed_rate = pass_completed_rate.strip()
        else:
            pass_completed_rate = ' '
        game_item['pass_completed_rate'] = pass_completed_rate

        # 积分
        game_item['points'] = ''

        time.sleep(3)
        yield game_item
