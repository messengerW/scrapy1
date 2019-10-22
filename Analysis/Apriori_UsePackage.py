"""
    File   : Apriori1.py
    Author : msw
    Date   : 2019/10/21 20:52
    Ps     : ...
    
"""
from apyori import apriori

data = [['豆奶','莴苣'],
        ['莴苣','尿布','葡萄酒','甜菜'],
        ['豆奶','尿布','葡萄酒','橙汁'],
        ['莴苣','豆奶','尿布','葡萄酒'],
        ['莴苣','豆奶','尿布','橙汁']]

result = list(apriori(transactions=data,min_support=0.5))
print(result)
