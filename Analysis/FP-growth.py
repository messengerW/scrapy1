"""
    File   : FP-Growth.py
    Author : msw
    Date   : 2019/10/26 16:18
    Ps     : ...
    
"""
from Analysis import getData


def loadSimpDat():
    datalist = [[0 for col in range(5)] for row in range(38)]
    data = getData.getDataset1(datalist)
    return data


def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        fset = frozenset(trans)
        retDict.setdefault(fset, 0)
        retDict[fset] += 1
    return retDict


class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}

    def inc(self, numOccur):
        self.count += numOccur

    def disp(self, ind=1):
        print('   ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)


def createTree(dataSet, minSup=1):
    headerTable = {}
    # 此一次遍历数据集， 记录每个数据项的支持度
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + 1

    # 根据最小支持度过滤
    lessThanMinsup = list(filter(lambda k: headerTable[k] < minSup, headerTable.keys()))
    for k in lessThanMinsup: del (headerTable[k])

    freqItemSet = set(headerTable.keys())
    # 如果所有数据都不满足最小支持度，返回None, None
    if len(freqItemSet) == 0:
        return None, None

    for k in headerTable:
        headerTable[k] = [headerTable[k], None]

    retTree = treeNode('φ', 1, None)
    # 第二次遍历数据集，构建fp-tree
    for tranSet, count in dataSet.items():
        # 根据最小支持度处理一条训练样本，key:样本中的一个样例，value:该样例的的全局支持度
        localD = {}
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]

        if len(localD) > 0:
            # 根据全局频繁项对每个事务中的数据进行排序,等价于 order by p[1] desc, p[0] desc
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: (p[1], p[0]), reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)
    return retTree, headerTable


def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:  # check if orderedItems[0] in retTree.children
        inTree.children[items[0]].inc(count)  # incrament count
    else:  # add items[0] to inTree.children
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None:  # update header table
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])

    if len(items) > 1:  # call updateTree() with remaining ordered items
        updateTree(items[1:], inTree.children[items[0]], headerTable, count)


def updateHeader(nodeToTest, targetNode):  # this version does not use recursion
    while (nodeToTest.nodeLink != None):  # Do not use recursion to traverse a linked list!
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode


def ascendTree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def findPrefixPath(basePat, headTable):
    condPats = {}
    treeNode = headTable[basePat][1]
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats


def mineTree(inTree, headerTable, minSup=1, preFix=set([]), freqItemList=[]):
    # order by minSup asc, value asc
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: (p[1][0], p[0]))]
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        # 通过条件模式基找到的频繁项集
        condPattBases = findPrefixPath(basePat, headerTable)
        myCondTree, myHead = createTree(condPattBases, minSup)
        if myHead != None:
            print('condPattBases: ', basePat, condPattBases)
            myCondTree.disp()
            print('*' * 30)

            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)


simpDat = loadSimpDat()
dictDat = createInitSet(simpDat)
myFPTree, myheader = createTree(dictDat, 3)
myFPTree.disp()
# condPats = findPrefixPath('z', myheader)
# print('z', condPats)
# condPats = findPrefixPath('x', myheader)
# print('x', condPats)
# condPats = findPrefixPath('y', myheader)
# print('y', condPats)
# condPats = findPrefixPath('t', myheader)
# print('t', condPats)
# condPats = findPrefixPath('s', myheader)
# print('s', condPats)
# condPats = findPrefixPath('r', myheader)
# print('r', condPats)

mineTree(myFPTree, myheader, 3)
