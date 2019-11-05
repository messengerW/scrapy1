"""
    File   : Exam_1.py
    Author : msw
    Date   : 2019/10/29 21:13
    Ps     :《数据仓库与数据挖掘》-实验一-数据预处理
            1)首先根据样本的最后一项特征(Defective)的值将样本分为：有缺陷样本/无缺陷样本;
            2)计算近邻值 k 并返回;
            3)计算每一条缺陷样本的所有标准欧氏距离,以二维列表(Double_List)的形式返回结果;
            4)对 Double_List 的每一行(代表一条缺陷样本)分别进行排序, 找出每一行最小的 k 个标准欧氏距离,
              这 k 个值对应的样本即为本条缺陷样本的近邻样本, 把这 k 个值的样本序号存在 adjacent_sample
              中, 最终返回结果二维列表 adjacent_sample
            5)根据 adjacent_sample 中的近邻样本序号, 计算特征差值, 更新特征权重
            6)最终对特征权重进行降序排序, 打印显示结果.

"""
from scipy.io import arff
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist

globals = {
    'nan': 0
}

def getStandardizedEDList(dataframe):
    """
    计算每一条缺陷样本的标准欧氏距离
    :param dataframe:所有样本 (type:dataframe)
    :return: 1) k:近邻数 (type:int)
             2) Double_List:所有缺陷样本的标准欧氏距离(42×302) (type:2D-list)
             3) df1:所有缺陷样本 (type:dataframe)
             4) df2:所有无缺样本 (type:dataframe)
    """
    # 根据 Defective 值进行分类, Y-有缺陷样本 / N-无缺陷样本
    dataframe1 = dataframe.loc[df['Defective'] == b'Y']
    dataframe2 = dataframe.loc[df['Defective'] == b'N']

    # 删除每个样本的最后一项特征值
    df1 = dataframe1.drop(columns='Defective')  # 有缺陷样本
    df2 = dataframe2.drop(columns='Defective')  # 无缺陷样本

    # 近邻数
    k = len(df2) / len(df1)

    vec1 = np.array(df1)
    vec2 = np.array(df2)

    # 一共有 len(ver1)=42个缺陷样本,每个缺陷样本需计算它的len(ver2)=302个标准化欧氏距离
    # 声明一个 42×302 大小的二维矩阵,存储每个样本的 302 个标准化欧氏距离
    Double_List = [[0 for col in range(len(vec2))] for row in range(len(vec1))]

    for i, v1 in enumerate(vec1):
        for j, v2 in enumerate(vec2):
            Vec = np.vstack([v1, v2])

            # method-1:公式计算
            # sk = np.var(Vec, axis=0, ddof=1)
            # sed = np.sqrt(((v1 - v2) ** 2 / sk).sum())
            # method-2:调用库
            sed = pdist(Vec,'seuclidean')
            Double_List[i][j] = sed
    # print(Standardized_ED_List, len(Standardized_ED_List), len(Standardized_ED_List[0]))
    return k, Double_List, df1, df2

def changeToTupleList(_list):
    """
    因为这次实验中很多排序都需要记录下标值，比如说对标准欧氏距离排序，排序的目的是得到最小的k个标准欧氏距离
    对应的样本序号，所以我先把列表从
    [value1,value2,...,valueN]
    转化为
    [(index1,value1), (index2,value2),...,(indexN,valueN)].
    这样对 value 排序后仍然保留原来的索引值。
    +++++++++++++++++++++++++++++++++++++++++
    + 其实有更好的方法：numpy.argsort()函数     +
    +    arr = [2,1,4,5,7,3,6]              +
    +    print(np.sort(arr))                +
    +    print(np.argsort(arr))             +
    +++++++++++++++++++++++++++++++++++++++++
    :param _list:
    :return:
    """
    for _index, _value in enumerate(_list):
        index_value = '({0},{1})'.format(_index, _value)
        _tuple = eval(index_value, globals)
        _list[_index] = _tuple
    return _list

# 自定义排序的规则
def ruler(elem):
    return elem[1]


def getAdjacentSample(k, Standardized_ED_List):
    """
    对每一条缺陷样本的302个标准欧氏距离进行升序排序
    :param k:近邻值 (type:int)
    :param Standardized_ED_List:标准欧氏距离列表 (42×302) (type:2D-list)
    :return: 每条缺陷样本的邻近样本id列表 (42×k) (type:2D-list)
    """
    adjacent_sample = [[0 for col in range(int(k))] for row in range(42)]
    # 遍历每一条缺陷样本，获取样本 id 以及此样本对应的标准欧氏距离列表(列表大小302)
    for sample_id, sample_sed_list in enumerate(Standardized_ED_List):
        # print(sample_id, sample_sed_list, end='\n\n\n')
        # 原本的列表只包含标准欧氏距离值，没有对应的样本id，即 sample_sed_list = [value1, value2, value3, ...]
        # 这里扩展 sample_sed_list = [(id1,value1),(id2,value2),(id3,value3),...]
        sample_sed_list = changeToTupleList(sample_sed_list)
        # 对 sed_list_withID 中的所有元组(id,value)进行升序排序，依据的关键字是 value
        sample_sed_list.sort(key=ruler)
        # print(sample_id, sed_list_withID[:int(k)])

        # 存储邻近样本的 id
        # item[0] 是 样本id, item[1] 是 sed 值
        for col, item in enumerate(sample_sed_list[:int(k)]):
            adjacent_sample[sample_id][col] = item[0]
            # print(df2.iloc[item[0]])

    return adjacent_sample


def calculateDiff(aslist, dataframe1, dataframe2):
    """
        这个函数作用是计算并特征差值并更新特征权重。一共有42条缺陷样本，每条缺陷样本有7个近邻样本，每个近邻样本
    又有37个特征值.
        我的想法是把这37个特征值组成一个series存到 dataframe1(42×37)的最后一行,然后一共要更新
    42(第一个for循环) × 7(第二个for循环) 次
        每次更新操作: 计算出37个特征差值 -> 求绝对值 -> 排序 -> 赋权重(1~37) -> 累加 ->更新 dataframe1

    :param aslist:近邻样本id列表 (42×7) (type:list)
    :param dataframe1:缺陷样本 (42×37) (type:dataframe)
    :param dataframe2:无缺样本 (302×37) (type:dataframe)
    :return:特征权重列表 (1×37)
    """
    DiffWeight = [0 for row in range(37)]
    for i in range(len(dataframe1)):
        # 根据行号依次从 dataframe1 中取出每一条缺陷样本 sampleY (type:series)
        sampleY = dataframe1.iloc[i]
        # 获取这条缺陷样本对应的近邻样本 id 列表
        adjacentlist = aslist[i]
        # 遍历近邻样本 id 列表, 依次获取当前缺陷样本的每一条近邻样本的 id
        for sample_id in adjacentlist:
            # 根据近邻样本的 id 从 dataframe2 中取出每一条近邻样本 sampleN (type:series)
            sampleN = dataframe2.iloc[sample_id]
            # 声明一个 1×37 的一维列表存储特征差值序列
            # diffvaluelist = [-1 for row in range(37)]
            # 计算特征差值
            delt = sampleY - sampleN
            # 取绝对值
            delt = np.abs(delt)
            # series 转 list
            diffvaluelist = delt.values.tolist()
            # 列表元组化
            diffvaluelist = changeToTupleList(diffvaluelist)

            # 对列表排序之前先复制一个副本
            # 最开始是这样写的，发现有问题，这样写两个列表应该是指向同一块内存地址的，本质上是同一个列表
            # copylist = diffvaluelist
            # 调用 list 的 copy() 函数，得到的是列表的一个副本，指向不同内存
            copylist = diffvaluelist.copy()
            # 对特征差值列表进行升序排序
            diffvaluelist.sort(key=ruler)
            # 根据特征差值序列更新特征权重列表, feature_tuple[0]:feature_id, feature_tuple[1]:feature_value
            for feature_tuple in copylist:
                _id = feature_tuple[0]
                _weight = diffvaluelist.index(feature_tuple)+1
                DiffWeight[_id] = DiffWeight[_id] + _weight

    return DiffWeight


def sortFeature(dataframe1, DiffWeight):
    """
    根据特征权重列表对特征进行排序(降序)
    :param dataframe1:存储所有缺陷样本的 dataframe (type:dataframe)
    :param DiffWeight:特征权重列表(1×37) (type:list)
    :return:所有特征的最终排序结果
    """
    # 列表元组化
    DiffWeight = changeToTupleList(DiffWeight)
    # 对元组化的列表降序排序,依据的关键字依然是元组的第二个元素(特征值)
    DiffWeight.sort(key=ruler, reverse=True)
    # 通过获取 dataframe1 的每一列列名称得到所有特征的名称列表
    FeatureList = dataframe1.columns.values.tolist()
    # 行名称(行号)
    # RowNumberList = dataframe1._stat_axis.values.tolist()
    # 最终结果列表
    Result = []
    for _tuple in DiffWeight:
        Result.append(FeatureList[_tuple[0]])
    # 打印验证一下
    print(DiffWeight)
    return Result


if __name__ == '__main__':
    # 获取数据
    file = 'CM1.arff'
    data = arff.loadarff(file)
    df = pd.DataFrame(data[0])

    # 先调用 getStandardizedEDList() 函数获取以下数据:
    #   k: 近邻数,也就是每个缺陷样本拥有的近邻样本数
    #   Standardized_ED_List: 标准欧氏距离值列表 (42×302)
    #   df1: 存储所有缺陷样本的dataframe
    #   df2: 存储所有五缺陷样本的dataframe
    k, Standardized_ED_List, df1, df2 = getStandardizedEDList(df)

    # 调用 getAdjacentSample() 函数，得到一个包含每条缺陷样本对应近邻样本的id列表 (42×7)
    Adjacent_Sample_List = getAdjacentSample(k, Standardized_ED_List)
    # print(Adjacent_Sample_List)

    # 调用 calculateDiff() 函数，得到特征权重列表 (1×37)
    Diff_Weight_List = calculateDiff(Adjacent_Sample_List, df1, df2)

    # 最后调用 sortFeature() 函数，根据特征权重列表对所有特征进行排序，并返回最终结果列表
    result = sortFeature(df1, Diff_Weight_List)
    # 打印输出
    # print(result)
