"""
    File   : eee.py
    Author : msw
    Date   : 2019/12/10 10:48
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
from sklearn.model_selection import StratifiedKFold, train_test_split
from Test.Course import Exam1


def eval(file):

    # 解析文件
    data = arff.loadarff(file)

    # 获取 dataframe 格式的数据集
    df = pd.DataFrame(data[0])

    # test1 - 使用全部属性
    X = df.drop(columns='Defective')

    # 样本标签(真是分类)
    df.loc[df['Defective'] == b'N'] = 0
    df.loc[df['Defective'] == b'Y'] = 1
    y = df.Defective

    features = X.columns.values.tolist()


    xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

    clf = tree.DecisionTreeClassifier()
    clf.fit(xtrain, ytrain)

    # 可视化
    with open('./exam3.dot', 'w', encoding='utf-8') as f:
        f = tree.export_graphviz(clf, feature_names=features, out_file=f)

if __name__ == '__main__':

    # 数据集
    file = './CM1.arff'

    eval(file)