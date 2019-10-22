"""
    File   : Learn_pandas.py
    Author : msw
    Date   : 2019/10/21 15:50
    Ps     : ...
    
"""
import pandas as pd
from pandas import DataFrame

data = pd.read_excel('test.xlsx', sheet_name='Sheet1')
print(data)
print("++++++++++++++++++")

data['sum'] = data['Age'] + data['Sex']
print(data)

DataFrame(data).to_excel('test.xlsx',index=False,header=True)