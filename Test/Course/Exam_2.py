"""
    File   : Exam_2.py
    Author : msw
    Date   : 2019/11/5 13:24
    Ps     : ...

"""
from Analysis import getData


def loadDataSet():
    """
    获取数据
    :return:返回一个包含若干事物的二维列表
    """

    data = [['牛奶', '啤酒', '尿布'],
            ['牛奶', '面包', '黄油'],
            ['牛奶', '尿布', '饼干'],
            ['面包', '黄油', '饼干'],
            ['啤酒', '尿布', '饼干'],
            ['牛奶', '尿布', '面包', '黄油'],
            ['尿布', '面包', '黄油'],
            ['啤酒', '尿布'],
            ['牛奶', '尿布', '面包', '黄油'],
            ['啤酒', '饼干'],
            ]

    data = [['黄河鲤鱼', '北京烤鸭', '大拌菜', '麻婆豆腐', '红烧肥肠', '啤酒 '],
            ['大拌菜', '麻婆豆腐', '红烧肥肠', '米饭', '啤酒'],
            ['黄河鲤鱼', '北京烤鸭', '大拌菜'],
            ['北京烤鸭', '大拌菜', '麻婆豆腐', '红烧肥肠', '啤酒'],
            ['麻婆豆腐', '红烧肥肠', '米饭', '啤酒'],
            ]
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
    计算Ck中的项集在数据集合D(记录或者transactions)中的支持度,返回满足最小支持度的项集的集合
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
    :param Lk:待连接的频繁相机
    :param k:频繁项集的项数
    :return:
    """
    retList = []
    for i in range(len(Lk)):
        for j in range(i + 1, len(Lk)):
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
    :param dataSet: 事物列表
    :param minSupport: 最小支持度
    :return: 返回频繁项集列表，以及支持度字典
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


def generate_big_rules(L, supportData, minConf):
    """
    从频繁相机中提取出所有满足最小支持度阈值的关联规则
    :param L: 频繁相机
    :param supportData:支持度列表
    :param minConf: 最小支持度
    :return:
    """
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = supportData[freq_set] / supportData[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= minConf and big_rule not in big_rule_list:
                        # print freq_set-sub_set, " => ", sub_set, "conf: ", conf
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list

if __name__ == '__main__':

    minSup = 0.5        # 最小支持度
    minConf = 0.8       # 最小置信度

    dataSet = loadDataSet()
    L, suppData = apriori(dataSet, minSup)
    rules = generate_big_rules(L, suppData, minConf)

    for i, _list in enumerate(L):
        print("频繁" ,i + 1, "项集：")
        for _elem in _list:
            print(_elem, "support: ", suppData[_elem])
        print('关联规则：')
        for rule in rules:
            if (len(rule[0]) + len(rule[1])) == i+1:
                print(rule[0], "=>", rule[1], "confidence: ", rule[2])
        print('='*80)