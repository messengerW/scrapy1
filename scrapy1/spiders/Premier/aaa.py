"""
    File   : aaa.py
    Author : msw
    Date   : 2019/9/21 13:59
    Ps     : ...
    
"""
import requests

link = 'http://www.httpbin.org/post'
header = {'param1':'v1', 'param2':'v2', 'param3':'v3'}
r = requests.get(url=link,data=header)

print("link:",r.url)
print("content:",r.text)
