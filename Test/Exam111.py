"""
    File   : Exam111.py
    Author : msw
    Date   : 2019/10/29 12:24
    Ps     : ...
    
"""
from scipy.io import arff
import pandas as pd
import numpy as np

# 获取数据
data = arff.loadarff('CM1.arff')
df = pd.DataFrame(data[0])
# print(df, type(df))
# print(type(df['Defective']))

# 根据 Defective 值进行分类, Y-有缺陷样本 / N-无缺陷样本
df1 = df.loc[df['Defective'] == b'Y']
df2 = df.loc[df['Defective'] == b'N']

# 删除每个样本的最后一项特征值
df1 = df1.drop(columns='Defective')  # 有缺陷样本
df2 = df2.drop(columns='Defective')  # 无缺陷样本

# print(df1, type(df1))
# print(df2, type(df2))

k = len(df2) / len(df1)

vec1 = np.array(df1)
# print(type(vec1),vec1)
vec2 = np.array(df2)
# print(type(vec2),len(vec2),vec2)

# 一共有 len(ver1)=42个缺陷样本,每个缺陷样本需计算它的len(ver2)=302个标准化欧氏距离
# 声明一个 42×302 大小的二维矩阵,存储每个样本的 302 个标准化欧氏距离
Standardized_ED_List = [[0 for col in range(len(vec2))] for row in range(len(vec1))]
# 再声明一个 42×k 的二维矩阵，存储每条缺陷样本对应的 k 个
# Adjacent_Sample_List = [[0 for col in range(int(k))] for row in range(len(vec1))]

for i, v1 in enumerate(vec1):
    for j, v2 in enumerate(vec2):
        Vec = np.hstack([v1, v2])
        sk = np.var(Vec, axis=0, ddof=1)
        sed = np.sqrt(((v1 - v2) ** 2 / sk).sum())
        Standardized_ED_List[i][j] = sed
# print(Standardized_ED_List, len(Standardized_ED_List), len(Standardized_ED_List[0]))

def sortRule(elem):
    return elem[1]

# 遍历每一条缺陷样本，获取样本 id 以及此样本对应的标准欧氏距离列表(列表大小302)
for sample_id, sample_sed_list in enumerate(Standardized_ED_List):
    # print(sample_id, sample_sed_list, end='\n\n\n')

    # 原本的列表只包含标准欧氏距离值，没有对应的样本id，即 sample_sed_list = [value1, value2, value3, ...]
    sed_list_withID = []
    # 这里扩展 sample_sed_list 为 sed_list_withID，即 sed_list_withID = [(id1,value1),(id2,value2),(id3,value3),...]
    for sed_id, sed_value in enumerate(sample_sed_list):
        sed_id_value = '({0},{1})'.format(sed_id, sed_value)
        _tuple = eval(sed_id_value)
        sed_list_withID.append(_tuple)
    # 对 sed_list_withID 中的所有元组(id,value)进行升序排序，依据的关键字是 value
    sed_list_withID.sort(key=sortRule)
    # print(sample_id, sed_list_withID[:int(k)])

    # 用于存储邻近样本的 id
    adjacent_sample = []
    for item in sed_list_withID[:int(k)]:
        adjacent_sample.append(item[0])
        # print(df2.iloc[item[0]])
    # print(adjacent_sample)
    # print('\n\n')

    for index in range(len(df1)):
        print(df1.iloc[i].values, len(df1.iloc[i]), type(df1.iloc[i].values))

























# Vec = np.vstack([vec1, vec2])
# sk = np.var(Vec, axis=0, ddof=1)
# ed1 = np.sqrt(((vec1 - vec2) ** 2 / sk).sum())
# print(str(ed1))

# Vec = np.vstack([vec1, vec2])
# dist = pdist(Vec, 'seuclidean')
# print('标准化欧式距离测试结果：' + str(dist), type(dist))
# print(len(list(dist)))
