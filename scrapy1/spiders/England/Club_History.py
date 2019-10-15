"""
    File   : Club_History.py
    Author : msw
    Date   : 2019/10/14 20:04
    Ps     : 本周讨论后决定做回归分析，需要用到以往赛季的数据，分析了一下请求 url，season 改一下
            就是以往赛季的数据，然后更改 stageName 就可以爬取以往赛季每一轮的球队数据了。
    
"""

import re
import json
import time
import scrapy
import random
from scrapy import Request
from scrapy1.items import ClubTurnItem


class ClubHistorySpider(scrapy.Spider):
    name = 'spider_clubhistory'

    # 最开始的 request 页面
    url = 'http://www.tzuqiu.cc/matchTeamStatistics/querysStat.json?comeptitionId=1&season=16%2F17&stageName=1'

    def start_requests(self):
        yield Request(self.url)

    def parse(self, response):
        # 获取到请求页面的所有数据并转化格式
        datas = json.loads(response.body)
        item = ClubTurnItem()
        # 随机sleep，方式被 ban
        time.sleep(1 + random.random())
        # 判断是否为空，不为空则提取出数据
        if datas:
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

        # 获取当卡请求的赛季，例如 18-19
        year1 = re.search(r'season=(\d+)', response.url).group(1)
        year2 = re.search(r'%2F(\d+)', response.url).group(1)
        # 获取到当前的轮次
        turn = re.search(r'(\d+)$', response.url).group()
        # 判断，如果轮次 turn<38 则轮次加一
        if int(turn) < 38:
            turn = str(int(turn) + 1)
            nexturl = re.sub(r'(\d+)$', turn, response.url)
            print("nexturl = %s" % nexturl)
            yield Request(nexturl)
        # 如果 turn>38 则需要修改赛季，并把 turn 重置为 1
        else:
            turn = str(1)
            year1 = 'season=' + year2
            year2 = '%2F' + str(int(year2) + 1)
            nexturl = re.sub(r'(\d+)$', turn, response.url)
            nexturl = re.sub(r'season=(\d+)', year1, nexturl)
            nexturl = re.sub(r'%2F(\d+)', year2, nexturl)
            print("nexturl = %s" % nexturl)
            yield Request(nexturl)
