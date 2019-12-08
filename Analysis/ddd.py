"""
    File   : ddd.py
    Author : msw
    Date   : 2019/12/8 17:50
    Ps     : ...
    
"""
import pandas as pd
from Analysis import DecisionTree
from scipy.io import arff
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold, cross_val_score, StratifiedKFold

# 加载数据集文件
file = '../Test/Data/CM1.arff'

# 解析文件
data = arff.loadarff(file)
# 获取 dataframe 格式的数据集
df = pd.DataFrame(data[0])

# 获取 labels 列表
features = ['HALSTEAD_DIFFICULTY', 'HALSTEAD_LEVEL', 'HALSTEAD_PROG_TIME', 'HALSTEAD_ERROR_EST', 'NUM_OPERANDS']
X = df[features]

df.loc[df['Defective'] == b'N'] = 0
df.loc[df['Defective'] == b'Y'] = 1
y = df.Defective

skf = StratifiedKFold(n_splits=10)
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X.loc[train_index, :], X.loc[test_index, :]
    y_train, y_test = y[train_index], y[test_index]
    v10 = cross_val_score(DecisionTreeClassifier(), X_train, y_train, cv=10).mean()
    print(v10)