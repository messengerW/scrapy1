"""
    File   : DecisionTree.py
    Author : msw
    Date   : 2019/12/3 10:45
    Ps     : ...

"""
import graphviz
import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn import tree
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold
from Test.Course import Exam1


def eval(filepath, features, classifier):
    """
    评价分类器的分类效果: 首先先对数据集进行处理,取出features标签列表(实验一得到的前log2d项特征)对应的列,
    然后得到数据集最后一列(label),对label做数值化处理,1代表有缺陷,0代表无缺陷.然后对数据集进行切分,切分成
    大小相似的10份子集,进行10折交叉验证,分别使用决策树和贝叶斯分类构建模型。最后对模型预测结果进行评估,采用
    F值、ROC_AUC、精确率和召回率四种评价指标。

    :param filepath: 数据集所在文件的路径
    :param features: 由实验一得到的前 log2d 项特征
    :param classifier: 分类预测使用的分类器
    :return: 十折交叉预测将数据集分成大小相似的十分不相交的子集,每一份子集依次作为测试集,然后
            预测、打分,最终将评分记录至 scores 列表
    """
    # 解析文件
    data = arff.loadarff(filepath)
    # 获取 dataframe 格式的数据集
    df = pd.DataFrame(data[0])

    # test1 - 使用全部属性
    X = df.drop(columns='Defective')

    # test2 - 使用由 Exam1 筛选后的前 log2d 个属性
    X = df[features]

    # 样本标签(真是分类)
    df.loc[df['Defective'] == b'N'] = 0
    df.loc[df['Defective'] == b'Y'] = 1
    y = df.Defective

    # 切分数据集, n_splits为份数
    skf = StratifiedKFold(n_splits=10,shuffle=True)

    scores = []
    f1_scores = []
    roc_scores = []
    accu_scores = []
    recall_scores = []

    # skf.split(X, y)是一个迭代器,返回的是 n_splits 组下标序列, 每组下标序列由两部分组成:
    # 训练集(9份)所有样本序号: train_index
    # 测试集(1份)所有样本序号: test_index
    for train_index, test_index in skf.split(X, y):
        # 根据划分结果从数据集中取出每一次分类预测的训练集、测试集
        X_train, X_test = X.loc[train_index, :], X.loc[test_index, :]
        y_train, y_test = y[train_index], y[test_index]
        # 训练模型
        classifier.fit(X_train, y_train)
        # 对测试集进行预测
        predict = classifier.predict(X_test)
        # 评估
        f1_scores.append(metrics.f1_score(y_test, predict))     # f1值
        roc_scores.append(metrics.roc_auc_score(y_test,predict))    # ROC_AUC
        accu_scores.append(metrics.accuracy_score(y_test,predict))  # 精确率
        recall_scores.append(metrics.recall_score(y_test,predict))  # 召回率

        # 可视化
        # with open('./exam3.dot', 'w', encoding='utf-8') as f:
        #     f = tree.export_graphviz(classifier, feature_names=features, out_file=f)

    scores.append(np.array(f1_scores).mean())
    scores.append(np.array(roc_scores).mean())
    scores.append(np.array(accu_scores).mean())
    scores.append(np.array(recall_scores).mean())

    return scores


if __name__ == '__main__':

    # 数据集
    filepath = '../Data/'
    filename = ['CM1','JM1','KC1','KC3','MC1','MC2','MW1','PC1','PC2','PC3','PC4','PC5']
    fileformat = '.arff'

    # 对每个数据集进行缺陷预测
    for fn in filename:
        file = filepath + str(fn) + fileformat
        # print(file)
        # 对每个数据集调用实验一代码,得到前 log2d 项特征
        features = Exam1.getLog2dfeature(file)
        # 分类器: 决策树 / 贝叶斯
        models = [DecisionTreeClassifier(), GaussianNB()]

        for model in models:
            scores = eval(file, features, model)
            print("DataSet : ", file)
            print("f1_scores : ", scores[0])
            print("roc_auc_score : ", scores[1])
            print("accuracy_score : ", scores[2])
            print("recall_score : ", scores[3])
            print('\n')
