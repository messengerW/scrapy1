"""
    File   : Apriori.py
    Author : msw
    Date   : 2019/10/21 20:23
    Ps     : ...
    
"""
from Analysis import getData


def loadDataSet():
    # 获取数据集，调用的是 getData 类中的 getDataset1() 方法
    datalist = [[0 for col in range(5)] for row in range(38)]
    data = getData.getDataset1(datalist)
    return data


def createC1(dataSet):
    """
    #生成候选 1-项集
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
    #计算Ck中的项集在数据集合D(记录或者transactions)中的支持度,返回满足最小支持度的项集的集合
     和所有项集支持度信息的字典。
    :param D:原始数据集
    :param Ck:候选集项Ck
    :param minSupport:支持度的最小值
    :return:
    """
    ssCnt = {}
    for tid in D:
        # 对于每一条transaction
        for can in Ck:
            # 对于每一个候选项集can，检查是否是transaction的一部分
            if can.issubset(tid):
                if can not in (ssCnt.keys()):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    Lk = []  # 候选集项Cn生成的频繁项集Lk
    supportData = {}  # 候选集项Cn的支持度字典
    # 计算候选项集的支持度, supportData key:候选项， value:支持度
    for key in ssCnt:
        # 计算每个项集的支持度
        support = ssCnt[key] / numItems
        # 将满足最小支持度的项集，加入Lk
        if support >= minSupport:
            Lk.insert(0, key)
        supportData[key] = support
    return Lk, supportData


def aprioriGen(Lk, k):
    """
    #连接操作，将频繁Lk-1项集通过拼接转换为候选k项集
    :param Lk:
    :param k:
    :return:
    """
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
    C1 = createC1(dataSet)  # 构建初始候选项集C1
    D = list(map(set, dataSet))  # 将dataSet集合化，以满足scanD的格式要求
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2  # 最初的L1中的每个项集含有一个元素，新生成的项集应该含有2个元素，所以 k=2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)  # 将新的项集的支持度数据加入原来的总支持度字典中
        L.append(Lk)  # 将符合最小支持度要求的项集加入L
        k += 1
    return L, supportData


def calcConf(freqSet, H, supportData, brl, minConf):
    """
    #计算规则的可信度，返回满足最小可信度的规则。
    :param freqSet:频繁项集
    :param H:频繁项集中所有的元素
    :param supportData:频繁项集中所有元素的支持度
    :param brl:满足可信度条件的关联规则
    :param minConf:最小可信度
    :return:
    """
    prunedH = []
    # 用每个conseq作为后件
    for conseq in H:
        # 计算置信度
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print(freqSet - conseq, '-->', conseq, 'conf:', conf)
            # 元组中的三个元素：前件、后件、置信度
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


# 对规则进行评估
def rulesFromConseq(freqSet, H, supportData, brl, minConf):
    """
    #对频繁项集中元素超过2的项集进行合并。
    :param freqSet:频繁项集
    :param H:频繁项集中的所有元素，即可以出现在规则右部的元素
    :param supportData:所有项集的支持度信息
    :param brl:生成的规则
    :param minConf:最小可信度
    :return:
    """
    m = len(H[0])
    # 查看频繁项集是否大到移除大小为 m 的子集
    if len(freqSet) > (m + 1):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        # 如果不止一条规则满足要求，进一步递归合并
        if len(Hmp1) > 1:
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)


def generateRules(L, supportData, minConf):
    """
    #根据频繁项集和最小可信度生成规则。
    由于小于最小支持度的项集已经剔除，剩余项集形成的规则中如果大于设定的最小置信度阈值，则认为它们是强关联规则
    :param L:频繁项集列表
    :param supportData:包含频繁项集支持数据的字典
    :param minConf:最小置信度
    :return:
    """
    bigRuleList = []  # 包含置信度的规则列表
    # 从频繁二项集开始遍历
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if i > 1:
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList


if __name__ == '__main__':
    dataSet = loadDataSet()
    L, suppData = apriori(dataSet, 0.4)
    i = 0
    for one in L:
        print("项数为 %s 的频繁项集：" % (i + 1), one, "\n")
        i += 1

    rules = generateRules(L, suppData, 0.8)
