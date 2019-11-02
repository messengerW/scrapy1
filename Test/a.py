"""
    File   : a.py
    Author : msw
    Date   : 2019/10/30 19:48
    Ps     : ...
    
"""
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'id':[1,2,3,4,5,6],'value':[1,2,3,4,5,6]})
df2 = pd.DataFrame({'id':[1,4,5,7,1,1],'value':[3,4,8,1,4,1]})

print(df1)
print('\n\n')
print(df2)
print('\n\n')

n = df2.iloc[0]
for i in range(len(df1)):
    m = df1.iloc[i]
    r = m-n
    print((r))