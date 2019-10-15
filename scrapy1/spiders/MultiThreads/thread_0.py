# """
#     File   : thread_0.py
#     Author : msw
#     Date   : 2019/9/26 13:29
#     Ps     : 串行爬取 1000 个 url.不使用多线程
#     Tatal time :  1654.2648260593414
#
# """
# import time
# import requests
#
# link_list = []
#
# with open('uuurls.txt', 'r') as file:
#     file_list = file.readlines()
#     for each in file_list:
#         link = each.split('\t')[1]
#         link = link.replace('\n', '')
#         link_list.append(link)  # 将整理好的 url 放入 list
#
# start = time.time()
#
# def crawler():
#     for url in link_list:
#         try:
#             r = requests.get(url, timeout=20)
#             print(r.status_code, url)
#         except Exception as e:
#             print('Error:', e)
# crawler()
#
# end = time.time()
# print('Tatal time : ', end - start)
