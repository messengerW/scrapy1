"""
    File   : Apriori.py
    Author : msw
    Date   : 2019/10/21 20:23
    Ps     : ...
    
"""


def loadDataSet():
    """
    生成数据集
    :arg A : 控球率达到 65%
    :arg B : 传球成功率达到 85%
    :arg C : 射正 5 脚以上
    :arg D : 主场
    :arg E : 获得本场比赛胜利
    """
    return [['A', 'B', 'C', 'D', 'E'], ['B', 'C'], ['A', 'B', 'C', 'D', 'E'], [], ['C'],
            ['B', 'D', 'E'], ['C'], ['D'], [], ['A', 'B', 'C', 'D', 'E'], [],
            ['A', 'B', 'C', 'D', 'E'], ['C'], ['D', 'E'], ['A', 'B', 'C'], [],
            ['C', 'D', 'E'], ['B', 'C'], ['A', 'B', 'C', 'D', 'E'], ['C', 'D', 'E'],
            ['C', 'E'], ['A', 'B'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'D'], ['A', 'C'],
            ['A', 'B', 'C', 'D', 'E'], ['A', 'B'], ['B', 'C', 'D', 'E'], [], ['A', 'C', 'D', 'E'],
            ['C'], ['D', 'E'], ['A', 'C'], ['B', 'C', 'D', 'E'], ['A', 'B', 'C'],
            ['A', 'B', 'C', 'D', 'E'], ['A'], ['B', 'C', 'D', 'E']
            ]


def createC1(dataSet):
    """
    生成长度为1的所有候选项
    :param dataSet:
    :return:
    """
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))


def scanD(D, Ck, minSupport):
    """
    从候选项集中生成频繁项集，同时输出一个包含支持度值的字典
    :param D:
    :param Ck:
    :param minSupport:
    :return:
    """
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if can not in (ssCnt.keys()):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport):
    """
    得到频繁项的基础上，进一步将频繁项组合并计算支持度
    返回一个包含整个频繁项集的列表和频繁项集列表中每个元素对应的支持度值的字典
    :return:
    """
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


def generateRules(L, supportData, minConf=0.5):
    """
    由于小于最小支持度的项集已经剔除，剩余项集形成的规则中如果大于设定的最小置信度阈值，则认为它们是强关联规则
    :param L:
    :param supportData:
    :param minConf:
    :return:
    """
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if i > 1:
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList


def calcConf(freqSet, H, supportData, brl, minConf=0.5):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print(freqSet - conseq, '-->', conseq, 'conf:', conf)

            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.5):
    m = len(H[0])
    if len(freqSet) > (m + 1):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if len(Hmp1) > 1:
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)


if __name__ == '__main__':
    dataSet = loadDataSet()
    L, suppData = apriori(dataSet, 0.3)
    i = 0
    for one in L:
        print("项数为 %s 的频繁项集：" % (i + 1), one, "\n")
        i += 1
