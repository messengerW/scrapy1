"""
    File   : CutLines.py
    Author : msw
    Date   : 2019/10/21 13:29
    Ps     : ...
    
"""
# import re
#
# reg = re.compile(r'[+-]?\d+')
#
# print(re.match(reg,"+100"))
# print(re.match(reg,"5e2"))
# print(re.match(reg,"-123"))
# print(re.match(reg,"3.1416"))
# print(re.match(reg,"-1E-16"))
# print(re.match(reg,"12e"))
# print(re.match(reg,"1a3.14"))
# print(re.match(reg,"1.2.3"))
# print(re.match(reg,"+-5"))
# print(re.match(reg,"12e+4.3"))

import numpy as np

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a[0:1])			# 截取第一行,返回 [[1 2 3 4 5]]
print(a[1,2:5])			# 截取第二行，第三、四、五列，返回 [8 9 10]
print(a[1,:])			# 截取第二行,返回 [ 6  7  8  9 10]
print(type(a))
print(a)