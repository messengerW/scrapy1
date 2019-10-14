"""
    File   : Club_Turn.py
    Author : msw
    Date   : 2019/9/20 17:43
    Ps     : 根据 Player_Turn 改写的，只有 url 变了，属性变了，而且也不用翻页了，一共就20条，使用的时候
             把 url 最后一个参数 stageName 改一下就行了，它的值对应轮次
    
"""
import re
import json
import time
import scrapy
from scrapy import Request
from scrapy1.items import ClubTurnItem

class PlayerTurnSpider(scrapy.Spider):
    name = 'spider_clubturn'

    def start_requests(self):
        url = 'http://www.tzuqiu.cc/matchTeamStatistics/querysStat.json?comeptitionId=1&season=19%2F20&stageName=5'
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