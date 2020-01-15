"""
    File   : Decision-Tree.py
    Author : msw
    Date   : 2019/12/6 14:53
    Ps     : ...
    
"""
import operator
import pandas as pd
from math import log
from scipy.io import arff
from Test.Course import decisionTreePlot as dtPlot


def createDataset():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['a', 'b']
    return dataSet, labels


def calcShannonEntropy(dataSet):
    # 先计算样本总个数
    numEntries = len(dataSet)
    labelCounts = {}
    # 遍历每一条样本，统计数据集中所有样本的类别
    for data in dataSet:
        currentLabel = data[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    # 初始化香农熵
    shannonEntropy = 0.0
    # 计算香农熵
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEntropy -= prob * log(prob, 2)
    return shannonEntropy


def splitDataSet(dataSet, axis, value):
    """
    @Function: 每一次挑选一个特征属性划分数据集(生成分支)后,都需要把数据集中对应的列删除。
    :param dataSet: 数据集
    :param axis: 列索引
    :param value: 列值
    :return:
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            # 这两步的作用是获取剔除 axis 列属性后的特征向量
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            # 添加至列表末尾
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeature(dataSet):
    """
    @Function: 每次创建新分支时，根据一定的度量方式(信息增益、信息增益率、基尼指数)选择最优属性
    :param dataSet: 待划分的数据集
    :return: 最优特征的索引值
    """
    # 得到特征的个数,-1是因为每条样本的最后一项是所属标签而不是特征属性
    numFeatures = len(dataSet[0]) - 1
    # 计算当前熵
    baseEntropy = calcShannonEntropy(dataSet)
    # 初始化最高信息增益、最优特征
    bestInfoGain = 0.0
    bestFeature = -1

    # 遍历所有特征
    for i in range(numFeatures):
        # 将数据集中所有第 i 个特征存入特征值列表
        featList = [example[i] for example in dataSet]
        # 对上一步得到的特征值列表进行去重
        uniqueVals = set(featList)
        # 数据集依据当前特征划分后的新熵值
        newEntropy = 0.0

        # 遍历已去重的特征值列表
        for value in uniqueVals:
            # 按照当前 特征(i) 及其 特征值(value) 对数据集进行划分
            # 得到的subDataSet就是数据集中所有当前特征的取值为value( feature(i) = value )的样本集合
            subDataSet = splitDataSet(dataSet, i, value)
            # 权重, 数据集中第i个特征取值为value的样本占样本总体的比例,即出现的频率
            prob = len(subDataSet) / float(len(dataSet))
            # 累加求得最终的新熵
            newEntropy += prob * calcShannonEntropy(subDataSet)

        # 信息增益 = 划分前的熵 - 划分后的熵,可理解为数据集混乱度的减少程度
        infoGain = baseEntropy - newEntropy
        # 用当前特征的信息增益与最高信息增益作比较,更新最高信息增益、最优特征
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    """
    递归创建决策树
    :param dataSet: 数据集
    :param labels: 标签列表
    :return:
    """
    # 首先获得数据集中每一条样本所属的标签类,存入classList列表
    classList = [example[-1] for example in dataSet]
    # 讨论递归函数终止的两种情况(满足其一即可跳出递归):
    # condition-1: 标签列表中所有标签完全相同,即所有样本属于同一个类别
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # condition-2: 所有特征都被使用完了
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    # 从当前数据集中寻找最优特征
    bestFeat = chooseBestFeature(dataSet)
    # 最优特征对应的特征名映射
    bestFeatLabel = labels[bestFeat]
    # 创建 myTree 字典存储树的所有信息
    myTree = {bestFeatLabel: {}}
    # 从标签列表中删除当前最优特征对应的标签名
    del labels[bestFeat]
    # 本次生成新的分支所选用的最优特征索引值:bestFeat,遍历数据集得到每条样本的最优特征值
    featValues = [example[bestFeat] for example in dataSet]
    # 去重
    uniqueVals = set(featValues)
    # 遍历去重后的最优特征值列表
    for value in uniqueVals:
        # 为了保证每次调用createTree()时不改变原列表的内容(del),创建一个labels的副本
        subLabels = labels[:]
        # 依据最优特征及其特征取值划分后的数据集
        splitedDataSet = splitDataSet(dataSet, bestFeat, value)
        # 在每个数据集划分上递归调用createTree()函数
        myTree[bestFeatLabel][value] = createTree(splitedDataSet, subLabels)

    return myTree


def test0():
    """
    使用CreateDataset生成的默认数据集
    :return:
    """
    myData, labels = createDataset()
    myTree = createTree(myData, labels)
    print(myTree)
    dtPlot.createPlot(myTree)


def test1():
    """
    Use dataset1: CM1.arff
    :return:
    """
    # 加载数据集文件
    file = '../Test/Data/CM1.arff'
    # 解析文件
    data = arff.loadarff(file)
    # 获取 dataframe 格式的数据集
    df = pd.DataFrame(data[0])
    # 将数据集格式转为 二维列表
    datalist = df.values.tolist()
    # 获取 labels 列表
    featlabels = df.columns.values.tolist()

    # kf = KFold(n_splits=10, shuffle=False, random_state=50)
    # for train_index, test_index in kf.split(df):
    #     print('train', len(train_index), 'test', len(test_index))

    myTree = createTree(datalist, featlabels)
    dtPlot.createPlot(myTree)

    print(myTree)

if __name__ == "__main__":
    # test0()
    test1()
