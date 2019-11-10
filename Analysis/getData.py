"""
    File   : getData.py
    Author : msw
    Date   : 2019/10/22 22:39
    Ps     : 这个类的作用是读取文件(excel/csv/txt),并以列表的形式返回数据集,供其他函数调用
    
"""
import re
import pandas as pd


def getDataset1(dataset):
    """
    :param dataset: 接收传来的空列表，将从Excel中读取到的数据清洗后存入dataset
    :return: 返回数据集，格式为列表

    """

    data = pd.read_excel('D:/PyCharm 2017.3.3/proj/scrapy1/Analysis/liverpool.xlsx', sheet_name='game')
    # print(data)

    possessionList = data['possession'].values.tolist()
    passcompleteList = data['pass_completed_rate'].values.tolist()
    shootList = data['shoot_on_target'].values.tolist()
    homeawayList = data['home_or_away'].values.tolist()
    scoreList = data['score'].values.tolist()

    for i in range(38):
        """
            possession, 分为10档, A0:0~10%, A1:10%~20%, ...
            passcompleterate,分为10档, B0:0~10%, B1:10%~20%, ...
            shoot, 分为10档, C0:0~3, C1:4~6, ...
            homeaway D1:主场, D2:客场
            winorlose E1:胜, E2:平, E3:负
                     
        """
        # 控球率，分为 10 档
        possession = possessionList[i]
        if possession < 0.1:
            dataset[i][0] = 'A0'
        elif possession < 0.2:
            dataset[i][0] = 'A1'
        elif possession < 0.3:
            dataset[i][0] = 'A2'
        elif possession < 0.4:
            dataset[i][0] = 'A3'
        elif possession < 0.5:
            dataset[i][0] = 'A4'
        elif possession < 0.6:
            dataset[i][0] = 'A5'
        elif possession < 0.7:
            dataset[i][0] = 'A6'
        elif possession < 0.8:
            dataset[i][0] = 'A7'
        elif possession < 0.9:
            dataset[i][0] = 'A8'
        elif possession < 1.0:
            dataset[i][0] = 'A9'
        else:
            dataset[i][0] = '#'
            print('Error in dataset[%d][0]' % i)

        # 传球成功率，分为 10 档
        passcompleterate = passcompleteList[i]
        if passcompleterate < 0.1:
            dataset[i][1] = 'B0'
        elif passcompleterate < 0.2:
            dataset[i][1] = 'B1'
        elif passcompleterate < 0.3:
            dataset[i][1] = 'B2'
        elif passcompleterate < 0.4:
            dataset[i][1] = 'B3'
        elif passcompleterate < 0.5:
            dataset[i][1] = 'B4'
        elif passcompleterate < 0.6:
            dataset[i][1] = 'B5'
        elif passcompleterate < 0.7:
            dataset[i][1] = 'B6'
        elif passcompleterate < 0.8:
            dataset[i][1] = 'B7'
        elif passcompleterate < 0.9:
            dataset[i][1] = 'B8'
        elif passcompleterate < 1.0:
            dataset[i][1] = 'B9'
        else:
            dataset[i][1] = '#'
            print('Error in dataset[%d][1]' % i)

        # 射正数，分为 10 档
        shoot = shootList[i]
        if shoot < 3:
            dataset[i][2] = 'C0'
        elif shoot < 6:
            dataset[i][2] = 'C1'
        elif shoot < 9:
            dataset[i][2] = 'C2'
        elif shoot < 12:
            dataset[i][2] = 'C3'
        elif shoot < 15:
            dataset[i][2] = 'C4'
        elif shoot < 18:
            dataset[i][2] = 'C5'
        elif shoot < 21:
            dataset[i][2] = 'C6'
        elif shoot < 24:
            dataset[i][2] = 'C7'
        elif shoot < 27:
            dataset[i][2] = 'C8'
        elif shoot < 30:
            dataset[i][2] = 'C9'
        else:
            dataset[i][2] = '#'
            print('Error in dataset[%d][2]' % i)

        # 主客场
        homeaway = homeawayList[i]
        if homeaway == '主':
            dataset[i][3] = 'D1'
        elif homeaway == '客':
            dataset[i][3] = 'D2'
        else:
            dataset[i][3] = '#'
            print('Error in dataset[%d][3]' % i)

        # 胜平负这个需要稍做处理，具体的参考下面:由比分得出胜负
        score = scoreList[i]
        goals1 = re.match(r'(\d+)', score).group()
        goals2 = re.search(r'(\s)(\d+)', score).group(2)
        delt = int(goals1) - int(goals2)
        if delt > 0:
            dataset[i][4] = 'E1'
        elif delt == 0:
            dataset[i][4] = 'E2'
        else:
            dataset[i][4] = 'E3'

    return dataset


# 打印一下瞅瞅
# datalist = [[0 for col in range(5)] for row in range(38)]
# data = getDataset1(datalist)
# print(data)
