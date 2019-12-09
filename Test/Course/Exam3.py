"""
    File   : DecisionTree.py
    Author : msw
    Date   : 2019/12/3 10:45
    Ps     : ...

"""
import pandas as pd
from scipy.io import arff
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import StratifiedKFold


def eval(filepath, classifier):
    """
    评价分类器的分类效果
    :param filepath: 数据集所在文件的路径
    :param classifier: 分类预测使用的分类器
    :return: 十折交叉预测将数据集分成大小相似的十分不相交的子集,每一份子集依次作为测试集,然后
            预测、打分,最终将评分记录至 scores 列表
    """
    # 解析文件
    data = arff.loadarff(filepath)
    # 获取 dataframe 格式的数据集
    df = pd.DataFrame(data[0])

    # 使用全部属性
    X = df.drop(columns='Defective')

    # # 使用由 Exam1 筛选后的属性
    # features = ['HALSTEAD_DIFFICULTY', 'HALSTEAD_LEVEL', 'HALSTEAD_PROG_TIME', 'HALSTEAD_ERROR_EST', 'NUM_OPERANDS']
    # X = df[features]

    # 样本标签(真是分类)
    df.loc[df['Defective'] == b'N'] = 0
    df.loc[df['Defective'] == b'Y'] = 1
    y = df.Defective

    # 切分数据集, n_splits为份数
    skf = StratifiedKFold(n_splits=10)

    scores = []
    # skf.split(X, y)是一个迭代器,返回的是 n_splits 组下标序列, 每组下标序列由两部分组成:
    # 训练集(9份)所有样本序号: train_index
    # 测试集(1份)所有样本序号: test_index
    for train_index, test_index in skf.split(X, y):
        # 根据划分结果从数据集中取出每一次分类预测的训练集、测试集
        X_train, X_test = X.loc[train_index, :], X.loc[test_index, :]
        y_train, y_test = y[train_index], y[test_index]
        # 拟合
        classifier.fit(X_train, y_train)
        # 根据训练集中的数据进行预测
        predict = classifier.predict(X_test)
        # 评估
        # f1_score(y_true, y_pred) - F1值
        # y_true: 真实值,就是数据集最后一列的样本标签
        # y_pred: 预测值,可使用不同分类器进行预测
        score = metrics.f1_score(y_test, predict)
        scores.append(score)

    return scores


if __name__ == '__main__':

    file = '../Data/PC1.arff'
    models = [DecisionTreeClassifier(), GaussianNB()]

    for model in models:
        scores = eval(file, model)
        print(scores, end='\n\n')
