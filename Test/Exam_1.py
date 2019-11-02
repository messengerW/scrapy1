"""
    File   : Exam_1.py
    Author : msw
    Date   : 2019/10/29 21:13
    Ps     : ...
    
"""
from scipy.io import arff
import pandas as pd
import numpy as np


def getStandardizedEDList(dataframe):
    """
    计算每一条缺陷样本的标准欧氏距离
    :param dataframe:
    :return: k-近邻数 ，Double_List-存储着 42×302 个标准欧氏距离值 的二位列表
    """
    # 根据 Defective 值进行分类, Y-有缺陷样本 / N-无缺陷样本
    dataframe1 = dataframe.loc[df['Defective'] == b'Y']
    dataframe2 = dataframe.loc[df['Defective'] == b'N']

    # 删除每个样本的最后一项特征值
    df1 = dataframe1.drop(columns='Defective')  # 有缺陷样本
    df2 = dataframe2.drop(columns='Defective')  # 无缺陷样本

    # print(df1, type(df1))
    # print(df2, type(df2))

    k = len(df2) / len(df1)

    vec1 = np.array(df1)
    vec2 = np.array(df2)

    # 一共有 len(ver1)=42个缺陷样本,每个缺陷样本需计算它的len(ver2)=302个标准化欧氏距离
    # 声明一个 42×302 大小的二维矩阵,存储每个样本的 302 个标准化欧氏距离
    Double_List = [[0 for col in range(len(vec2))] for row in range(len(vec1))]


    for i, v1 in enumerate(vec1):
        for j, v2 in enumerate(vec2):
            Vec = np.hstack([v1, v2])
            sk = np.var(Vec, axis=0, ddof=1)
            sed = np.sqrt(((v1 - v2) ** 2 / sk).sum())
            Double_List[i][j] = sed
    # print(Standardized_ED_List, len(Standardized_ED_List), len(Standardized_ED_List[0]))
    return k, Double_List, df1, df2

def sortRule(elem):
    return elem[1]

def getAdjacentSample(k, Standardized_ED_List):
    """
    对每一条缺陷样本的302个标准欧氏距离进行降序排序
    :param k:近邻值
    :param Standardized_ED_List:标准欧氏距离列表
    :return: 返回一个列表-每条缺陷样本的邻近样本id
    """
    adjacent_sample = [[0 for col in range(int(k))] for row in range(42)]
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
        for col, item in enumerate(sed_list_withID[:int(k)]):
            adjacent_sample[sample_id][col] = item[0]
            # print(df2.iloc[item[0]])

    return adjacent_sample

def calculateDiff(aslist, dataframe1, dataframe2):
    """
        这个函数作用是计算并不断更新特征差值。一共有42条缺陷样本，每条缺陷样本有7个近邻样本，每个近邻样本又有
    38个特征值.
        我的想法是把这38个特征值组成一个series存到dataframe1(42×38)的最后一行,然后一共要更新
    42(第一个for循环) × 7(第二个for循环) 次
        每次更新操作: 计算出38个特征差值 -> 求绝对值 -> 排序 -> 赋权重(1~38) -> 累加 ->更新dataframe1
        
    :param aslist:近邻样本id列表 (42×7)
    :param dataframe1:缺陷样本 (42×38)
    :param dataframe2:无缺样本 (302×38)
    :return:
    """
    for i in range(len(dataframe1)):
        diffvalue_list = [[0 for col in range(38)] for row in range(7)]
        # 获取每一条缺陷样本
        sampleY = dataframe1.iloc[i]
        # 获取这条缺陷样本对应的近邻样本列表
        adjacentlist = aslist[i]
        # 遍历近邻样本id列表
        for sample_id in adjacentlist:
            # 获取每一条近邻样本
            sampleN = dataframe2.iloc[sample_id]


if __name__ == '__main__':
    # 获取数据
    data = arff.loadarff('CM1.arff')
    df = pd.DataFrame(data[0])

    k, Standardized_ED_List, df1, df2 = getStandardizedEDList(df)
    Adjacent_Sample_List = getAdjacentSample(k, Standardized_ED_List)
    # print(Adjacent_Sample_List,len(Adjacent_Sample_List))
    calculateDiff(Adjacent_Sample_List, df1, df2)