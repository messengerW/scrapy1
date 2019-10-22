"""
    File   : CutLines.py
    Author : msw
    Date   : 2019/10/21 13:29
    Ps     : ...
    
"""
import re
lines = "(|1|2|3|4|5|6|7|8|9|1|2|3|4|5|6|7|8|9|10|)"

# resault1 = lines.replace("|",")\n(")
_list = lines.split("|")
# print(resault1)
print(_list,len(_list))

# print(_list[0:3])
# print('|'.join(_list[0:3]))
# for i in range(0,int(1+len(_list)/3)):
#     sss = '|'.join(_list[i*3:(i+1)*3])
#     print(re.sub(r'\n',")\n(",sss))

print(len(_list)/3)
for i in range(1,int(len(_list)/3)):
    _list.insert(i*3+i,")\n(")
    newstr = '|'.join(_list)

print("====")
print(newstr)
print("+++++++++")
resault = re.sub(r'\(\|','(',newstr)
resault = re.sub(r'\|\)',')',resault)
# resault = re.sub(r'\n','-',resault)
print(resault)

_newlist = resault.split('\n')
print(_newlist)