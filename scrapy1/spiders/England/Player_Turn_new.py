"""
    File   : Player_Turn_new.py
    Author : msw
    Date   : 2019/9/21 15:36
    Ps     : 试一下，不用 scrapy 能不能完成 Player_Turn.py 的业务
    
"""
import re
import json
import time
import requests


def ajax_spider(url):
    r = requests.get(url=url)
    datas = json.loads(r.text)
    time.sleep(1)
    return datas

i = 0
for start in range(0,30):
    url1 = 'http://www.tzuqiu.cc/matchPlayerStatistics/querysStat.json?draw=1&columns%5B0%5D%5Bdata%5D=id&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=playerFormat&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=minsFormat&columns%5B2%5D%5Bname%5D=(mps.outTime+-+mps.inTime)&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=goalsFormat&columns%5B3%5D%5Bname%5D=mps.goals&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=assistsFormat&columns%5B4%5D%5Bname%5D=mps.assists&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=shotsFormat&columns%5B5%5D%5Bname%5D=mps.shots&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=passSuccFormat&columns%5B6%5D%5Bname%5D=mps.passSucc&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=bigChanceCreatedFormat&columns%5B7%5D%5Bname%5D=mps.bigChanceCreated&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=aerialsWonFormat&columns%5B8%5D%5Bname%5D=mps.aerialsWon&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=rateFormat&columns%5B9%5D%5Bname%5D=mps.rate&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=timelinesFormat&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=false&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&start='
    url2 = '&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&extra_param%5BcompetitionId%5D=1&extra_param%5Bseason%5D=19%2F20&extra_param%5BstageName%5D=5&_=1568884936712'
    url = url1 + str(start*10) + url2
    v = ajax_spider(url)
    if v['data']:  # 判断是否为空，不为空则提取出数据
        for data in v['data']:
            i = i+1
            name = data['playerName']
            print("%d.%s" % (i,name))