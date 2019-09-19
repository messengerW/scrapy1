"""
    File   : Player_Turn.py
    Author : msw
    Date   : 2019/9/19 17:46
    Ps     : 是根据 Player_Season 改写来的，与 Season 稍有不同：request url 多了一个参数
             （倒数第二个的 stageName，代表的是轮次），所以使用的时候，只需要把这个 stageName
             编辑一下就可以用了，用法和爬下来的数据和 Season 一样的。 比如现在是第 5 轮.
    
"""
import re
import json
import time
import scrapy
from scrapy import Request
from scrapy1.items import PlayerItem

class PlayerTurnSpider(scrapy.Spider):
    name = 'spider_playerturn'

    def start_requests(self):
        url = 'http://www.tzuqiu.cc/matchPlayerStatistics/querysStat.json?draw=1&columns%5B0%5D%5Bdata%5D=id&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=playerFormat&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=minsFormat&columns%5B2%5D%5Bname%5D=(mps.outTime+-+mps.inTime)&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=goalsFormat&columns%5B3%5D%5Bname%5D=mps.goals&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=assistsFormat&columns%5B4%5D%5Bname%5D=mps.assists&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=shotsFormat&columns%5B5%5D%5Bname%5D=mps.shots&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=passSuccFormat&columns%5B6%5D%5Bname%5D=mps.passSucc&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=bigChanceCreatedFormat&columns%5B7%5D%5Bname%5D=mps.bigChanceCreated&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=aerialsWonFormat&columns%5B8%5D%5Bname%5D=mps.aerialsWon&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=rateFormat&columns%5B9%5D%5Bname%5D=mps.rate&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=timelinesFormat&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=false&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&extra_param%5BcompetitionId%5D=1&extra_param%5Bseason%5D=19%2F20&extra_param%5BstageName%5D=5&_=1568884936712'
        yield Request(url)

    def parse(self, response):
        datas = json.loads(response.body)   # 获取到请求页面的所有数据并转化格式
        item = PlayerItem()
        time.sleep(1)

        if datas['data']:                           # 判断是否为空，不为空则提取出数据

            for data in datas['data']:
                item['playerMainPosition'] = data['playerMainPosition']
                item['teamName'] = data['teamName']
                item['offsides'] = data['offsides']
                item['bigChanceCreated'] = data['bigChanceCreated']
                item['seriousError'] = data['seriousError']
                item['thBall'] = data['thBall']
                item['crosses'] = data['crosses']
                item['passes'] = data['passes']
                item['teamId'] = data['teamId']
                item['keyPasses'] = data['keyPasses']
                item['yelCards'] = data['yelCards']
                item['aerialsWon'] = data['aerialsWon']
                item['rate'] = data['rate']
                item['longBall'] = data['longBall']
                item['interceptions'] = data['interceptions']
                item['age'] = data['age']
                item['clearances'] = data['clearances']
                item['shots'] = data['shots']
                item['fouled'] = data['fouled']
                item['accThB'] = data['accThB']
                item['accLB'] = data['accLB']
                item['finalThirdPass'] = data['finalThirdPass']
                item['finalThirdPassAcc'] = data['finalThirdPassAcc']
                item['blockShots'] = data['blockShots']
                item['totalTackles'] = data['totalTackles']
                item['fouls'] = data['fouls']
                item['assists'] = data['assists']
                item['playerName'] = data['playerName']
                item['passSucc'] = data['passSucc']
                item['penaltyScored'] = data['penaltyScored']
                item['mins'] = data['mins']
                item['accCrosses'] = data['accCrosses']
                item['goals'] = data['goals']
                item['shotsOT'] = data['shotsOT']
                item['errorsSum'] = data['errorsSum']
                item['playerId'] = data['playerId']
                item['matchId'] = data['matchId']
                item['offsideWon'] = data['offsideWon']
                item['redCards'] = data['redCards']
                item['disp'] = data['disp']
                item['dribbles'] = data['dribbles']
                item['fatalError'] = data['fatalError']
                item['unsTouches'] = data['unsTouches']

                yield item

            # 分析出点击下一个请求（下一页）时，只有这几个参数发生了变化
            # 用正则表达式索引、修改这几个参数
            _draw = re.search(r"draw=(\d+)", response.url).group(1)
            _start = re.search(r"start=(\d+)", response.url).group(1)
            _value = re.search(r"&_=(\d+)", response.url).group(1)

            _draw = 'draw=' + str(int(_draw) + 1)
            _start = 'start=' + str(int(_start) + 10)
            _value = '_=' + str(int(_value) + 1)
            nexturl = re.sub(r"draw=(\d+)", _draw, response.url)
            nexturl = re.sub(r"start=(\d+)", _start, nexturl)
            nexturl = re.sub(r"_=(\d+)", _value, nexturl)
            # 得到下一个请求url，然后发出请求
            yield Request(nexturl)