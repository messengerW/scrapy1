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


# 由比分得出胜负
scorelist = data['score'].values.tolist()
print(scorelist)
for item in scorelist:
    goals1 = re.match(r'(\d+)', str(item)).group()
    goals2 = re.search(r'(\s)(\d+)', str(item)).group(2)
    delt = int(goals1) - int(goals2)
    if delt > 0:
        winner = '主队 胜'
    elif delt < 0:
        winner = '客队 胜'
    else:
        winner = '平局'
    print("主队进球:%s，客队进球:%s，本场比赛 %s" % (goals1, goals2, winner))
