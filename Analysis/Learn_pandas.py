"""
    File   : Learn_pandas.py
    Author : msw
    Date   : 2019/10/21 15:50
    Ps     : ...
    
"""
import re
import pandas as pd
from pandas import DataFrame

# data = pd.read_excel('test.xlsx', sheet_name='Sheet1')
# print(data)
# print("++++++++++++++++++")
# data['sum'] = data['Age'] + data['Sex']
# print(data)
# DataFrame(data).to_excel('test.xlsx',index=False,header=True)

data = pd.read_excel('liverpool.xlsx', sheet_name='game')
# print(data)

'''
  创建一个 38 × 5 的二维列表, [控球率, 传球成功率, 射正数, 主客场, 胜平负]
    :param 控球率, 分为10档, A0：0~10%, A1：10%~20% ...
    :param 传球成功率,分为10档, B0, B1, B2 ...
    :param 射正数, 分为10档, C0:0~3, C1:4~6, C2 ...
    :param 主客场 D1:主场, D2:客场
    :param 胜平负 E1:胜, E2:平, E3:负
'''
overallList = [[0 for col in range(5)] for row in range(38)]
# print(OverallList)

possessionList = data['possession'].values.tolist()
passcompleteList = data['pass_completed_rate'].values.tolist()
shootList = data['shoot_on_target'].values.tolist()
homeawayList = data['home_or_away'].values.tolist()
scoreList = data['score'].values.tolist()

for i in range(38):
    
    possession = possessionList[i]
    if possession < 0.1:
        overallList[i][0] = 'A0'
    elif possession < 0.2:
        overallList[i][0] = 'A1'
    elif possession < 0.3:
        overallList[i][0] = 'A2'
    elif possession < 0.4:
        overallList[i][0] = 'A3'
    elif possession < 0.5:
        overallList[i][0] = 'A4'
    elif possession < 0.6:
        overallList[i][0] = 'A5'
    elif possession < 0.7:
        overallList[i][0] = 'A6'
    elif possession < 0.8:
        overallList[i][0] = 'A7'
    elif possession < 0.9:
        overallList[i][0] = 'A8'
    elif possession < 1.0:
        overallList[i][0] = 'A9'
    else:
        overallList[i][0] = '#'
        print('Error in overallList[%d][0]' % i)

    passcompleterate = passcompleteList[i]
    if passcompleterate < 0.1:
        overallList[i][1] = 'B0'
    elif passcompleterate < 0.2:
        overallList[i][1] = 'B1'
    elif passcompleterate < 0.3:
        overallList[i][1] = 'B2'
    elif passcompleterate < 0.4:
        overallList[i][1] = 'B3'
    elif passcompleterate < 0.5:
        overallList[i][1] = 'B4'
    elif passcompleterate < 0.6:
        overallList[i][1] = 'B5'
    elif passcompleterate < 0.7:
        overallList[i][1] = 'B6'
    elif passcompleterate < 0.8:
        overallList[i][1] = 'B7'
    elif passcompleterate < 0.9:
        overallList[i][1] = 'B8'
    elif passcompleterate < 1.0:
        overallList[i][1] = 'B9'
    else:
        overallList[i][1] = '#'
        print('Error in overallList[%d][1]' % i)

    shoot = shootList[i]
    if shoot < 3:
        overallList[i][2] = 'C0'
    elif shoot < 6:
        overallList[i][2] = 'C1'
    elif shoot < 9:
        overallList[i][2] = 'C2'
    elif shoot < 12:
        overallList[i][2] = 'C3'
    elif shoot < 15:
        overallList[i][2] = 'C4'
    elif shoot < 18:
        overallList[i][2] = 'C5'
    elif shoot < 21:
        overallList[i][2] = 'C6'
    elif shoot < 24:
        overallList[i][2] = 'C7'
    elif shoot < 27:
        overallList[i][2] = 'C8'
    elif shoot < 30:
        overallList[i][2] = 'C9'
    else:
        overallList[i][2] = '#'
        print('Error in overallList[%d][2]' % i)

    homeaway = homeawayList[i]
    if homeaway == '主':
        overallList[i][3] = 'D1'
    elif homeaway == '客':
        overallList[i][3] = 'D2'
    else:
        overallList[i][3] = '#'
        print('Error in overallList[%d][3]' % i)

    # 胜平负这个需要稍做处理，具体的参考下面:由比分得出胜负
    score = scoreList[i]
    goals1 = re.match(r'(\d+)',score).group()
    goals2 = re.search(r'(\:\s)(\d+)',score).group(2)
    delt = int(goals1) - int(goals2)
    if delt > 0:
        overallList[i][4] = 'E1'
    elif delt == 0:
        overallList[i][4] = 'E2'
    else:
        overallList[i][4] = 'E3'

print(overallList)

# 由比分得出胜负
# scorelist = data['score'].values.tolist()
# print(scorelist)
# for item in scorelist:
#     goals1 = re.match(r'(\d+)', str(item)).group()
#     goals2 = re.search(r'(\:\s)(\d+)', str(item)).group(2)
#     delt = int(goals1) - int(goals2)
#     if delt > 0:
#         winner = '主队 胜'
#     elif delt < 0:
#         winner = '客队 胜'
#     else:
#         winner = '平局'
#     print("主队进球:%s，客队进球:%s，本场比赛 %s" % (goals1, goals2, winner))
