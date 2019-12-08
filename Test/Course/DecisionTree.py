"""
    File   : DecisionTree.py
    Author : msw
    Date   : 2019/12/3 10:45
    Ps     : ...

"""
import pandas as pd
from scipy.io import arff
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score


def eval(filepath, classifier):
    # 解析文件
    data = arff.loadarff(filepath)
    # 获取 dataframe 格式的数据集
    df = pd.DataFrame(data[0])

    # 样本
    features = ['HALSTEAD_DIFFICULTY', 'HALSTEAD_LEVEL', 'HALSTEAD_PROG_TIME', 'HALSTEAD_ERROR_EST', 'NUM_OPERANDS']
    X = df[features]

    # 标签
    df.loc[df['Defective'] == b'N'] = 0
    df.loc[df['Defective'] == b'Y'] = 1
    y = df.Defective

    skf = StratifiedKFold(n_splits=10)

    scores = []
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X.loc[train_index, :], X.loc[test_index, :]
        y_train, y_test = y[train_index], y[test_index]
        ave_score = cross_val_score(classifier, X_train, y_train, cv=10).mean()
        scores.append(ave_score)

    return scores


if __name__ == '__main__':

    file = '../Data/CM1.arff'
    models = [DecisionTreeClassifier(), KNeighborsClassifier(), AdaBoostClassifier(),
              MLPClassifier(), RandomForestClassifier(), GaussianNB()]

    for model in models:
        scores = eval(file, model)
        print(scores,end='\n\n')
