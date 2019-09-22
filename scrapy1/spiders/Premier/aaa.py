"""
    File   : aaa.py
    Author : msw
    Date   : 2019/9/21 13:59
    Ps     : ...
    
"""
import re

line = "Fat cats are smarter than dogs, is it right?"
m = re.match(r'(.*) are (.*?) is',line)

print(m.group())
print(m.group(1))
print(m.group(2))
print(m.groups())
