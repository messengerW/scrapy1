"""
    File   : K-means.py
    Author : msw
    Date   : 2019/11/11 15:28
    Ps     : K-means Clustering

"""
from numpy import *
import matplotlib.pyplot as plt


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        # 简单处理，删除每一行首尾的空格并以 \t 分隔
        currtLine = line.strip().split('\t')
        # 浮点化
        fltLine = list(map(float, currtLine))
        dataMat.append(fltLine)
    return dataMat


def distEcludean(vecA, vecB):
    # 计算欧氏距离
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):
    # 为给定数据集构建一个包含K个随机质心的集合
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


def KMeans(dataSet, k, distMeas=distEcludean, createCent=randCent):
    # 确定行数（样本总数）
    m = shape(dataSet)[0]
    # 第一列存样本属于哪一簇
    # 第二列存样本的到簇的中心点的误差
    clusterAssment = mat(zeros((m, 2)))

    # 初始化centroids
    centroids = createCent(dataSet, k)
    clusterChanged = True

    while clusterChanged:
        clusterChanged = False

        # 遍历所有的样本（行数）
        for i in range(m):
            minDist = inf
            minIndex = -1

            # 遍历所有的质心
            # 找出最近的质心
            for j in range(k):
                # 计算该样本到质心的欧式距离
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j

            # 更新每一行样本所属的簇
            if clusterAssment[i, 0] != minIndex: clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        # print(centroids,end='\n\n')
        # 更新质心
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment


def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print
        "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print
        "Sorry! Your k is too large! please contact Zouxy"
        return 1

    # 绘制所有的样本
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # 绘制质心
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], '+', markersize=12)

    plt.show()


k = 4
daMat = mat(loadDataSet('testSet.txt'))
myCentroids, clustAssing = KMeans(daMat, k)
showCluster(daMat, k, myCentroids, clustAssing)
