"""
    File   : Exam1.py
    Author : msw
    Date   : 2019/10/29 10:10
    Ps     : 数据仓库与数据挖掘第一次上机 —— 数据预处理
             提交 源码 + word文档
    
"""
import re
import numpy
from scipy.spatial.distance import pdist

sample_list1 = []       # 有缺陷样本列表
sample_list2 = []       # 无缺陷样本列表

with open('CM1.arff','r') as reader:
    # 读取所有样本,并根据最后一项特征(Defective)分类, sample_list1 & sample_list2
    for i, line in enumerate(reader.readlines()[42:]):
        line = line.strip('\n')
        # 借助正则表达式，获取每个样本的最后一项特征值 Y-有缺陷 / N-无缺陷
        defective = re.search(r'[A-Z].?',line).group()
        # 去除最后一项特征值(Y/N)后的样本
        sample = re.search(r'(.*?),[YN]$',line).group(1)
        sample = sample.split(',')
        sample = list(map(float, sample))
        # 根据最后一项特征值 Defective 进行分类
        if defective == 'Y':
            sample_list1.append(sample)
        else:
            sample_list2.append(sample)
reader.close()

# 计算出近邻数, k = 无缺样本数/有缺陷样本数
k = len(sample_list2)/len(sample_list1)
# print(k,type(k))

# 一共有 len(sample_list1)=42个缺陷样本,每个缺陷样本需计算它的len(sample_list2)=302个标准化欧氏距离
# 所以先声明一个 42×302 大小的二维矩阵
Standardized_ED_List = [[0 for col in range(len(sample_list2))] for row in range(len(sample_list1))]
print(len(Standardized_ED_List),len(Standardized_ED_List[0]))

# print(len(sample_list1[0]),sample_list1[0])
# print(len(sample_list2[0]),sample_list2[0])
# vec1 = numpy.array(sample_list1[0],numpy.float64)
# vec2 = numpy.array(sample_list2[0],numpy.float64)
# Vec = numpy.vstack([vec1,vec2])
# print(Vec)

for sample1 in sample_list1:
    vec1 = numpy.array(sample1, numpy.float64)
    for sample2 in sample_list2:
        vec2 = numpy.array(sample2, numpy.float64)
        Vec = numpy.vstack([vec1, vec2])
        # print(Vec)
        sk = numpy.var(Vec, axis=0, ddof=1)
        ed1 = numpy.sqrt(((vec1 - vec2) ** 2 / sk).sum())
        print(ed1)
