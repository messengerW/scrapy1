"""
    File   : Club_History.py
    Author : msw
    Date   : 2019/10/14 20:04
    Ps     : 本周讨论后决定做回归分析，需要用到以往赛季的数据，分析了一下请求 url，season 改一下
            就是以往赛季的数据，然后更改 stageName 就可以爬取以往赛季每一轮的球队数据了。
    
"""

import json
import time
import scrapy
from scrapy import Request
from scrapy1.items import ClubTurnItem

class ClubHistorySpider(scrapy.Spider):
    name = 'spider_club_history'

    def start_requests(self):
        url = 'http://www.tzuqiu.cc/matchTeamStatistics/querysStat.json?comeptitionId=1&season=18%2F19&stageName=1'
        yield Request(url)

    def parse(self, response):
        datas = json.loads(response.body)   # 获取到请求页面的所有数据并转化格式
        item = ClubTurnItem()
        time.sleep(1)
        if datas:                           # 判断是否为空，不为空则提取出数据
            for data in datas:
                item['teamName'] = data['teamName']
                item['offsides'] = data['offsides']
                item['bigChanceCreated'] = data['bigChanceCreated']
                item['passes'] = data['passes']
                item['teamId'] = data['teamId']
                item['keyPasses'] = data['keyPasses']
                item['yelCards'] = data['yelCards']
                item['redCards'] = data['redCards']
                item['aerialsWon'] = data['aerialsWon']
                item['finalThirdPassAcc'] = data['finalThirdPassAcc']
                item['rate'] = data['rate']
                item['interceptions'] = data['interceptions']
                item['shots'] = data['shots']
                item['clearances'] = data['clearances']
                item['fouled'] = data['fouled']
                item['finalThirdPass'] = data['finalThirdPass']
                item['assists'] = data['assists']
                item['fouls'] = data['fouls']
                item['passSucc'] = data['passSucc']
                item['tacklesSuccful'] = data['tacklesSuccful']
                item['goalsLost'] = data['goalsLost']
                item['goals'] = data['goals']
                item['shotsOT'] = data['shotsOT']
                item['possession'] = data['possession']
                item['errorsSum'] = data['errorsSum']
                item['offsideWon'] = data['offsideWon']
                item['aerialDuelScc'] = data['aerialDuelScc']
                item['dribblesWon'] = data['dribblesWon']

                yield item

