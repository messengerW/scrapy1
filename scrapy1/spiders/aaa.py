"""
    File   : aaa.py
    Author : msw
    Date   : 2019/9/21 13:59
    Ps     : ...
    
"""
import re

url = "http://www.tzuqiu.cc/matchTeamStatistics/querysStat.json?comeptitionId=1&season=16%2F17&stageName=77"

year1 = re.search(r'season=(\d+)', url).group(1)
year2 = re.search(r'%2F(\d+)', url).group(1)

# 获取到当前的轮次
turn = re.search(r'(\d+)$', url).group()
print(year1)
print(year2)
print(turn)
# 判断，如果轮次 turn<38，则轮次加一 ; turn>38需要重置为 1，并修改赛季
if int(turn) < 38:
    turn = str(int(turn) + 1)
    nexturl = re.sub(r'(\d+)$', turn, url)
    print("nexturl = %s" % nexturl)
else:
    turn = str(1)
    year1 = 'season=' + year2
    year2 = '%2F' + str(int(year2) + 1)
    nexturl = re.sub(r'(\d+)$',turn,url)
    nexturl = re.sub(r'season=(\d+)',year1,nexturl)
    nexturl = re.sub(r'%2F(\d+)',year2,nexturl)
    print("nexturl = %s" % nexturl)

