# """
#     File   : thread1.py
#     Author : msw
#     Date   : 2019/9/25 21:01
#     Ps     : 学习一下多线程爬虫，这是书上的第一个实例。待爬的是1000个网站，分成了五份每份200个，然后开了
#              5个线程，每个线程分配200个url，各司其职。
#     Tatal time :  469.7220342159271
#
# """
# import time
# import threading
# import requests
#
# link_list = []
#
# with open('uuurls.txt', 'r') as file:
#     file_list = file.readlines()
#     for each in file_list:
#         link = each.split('\t')[1]
#         link = link.replace('\n', '')
#         link_list.append(link)
#
# start = time.time()
#
#
# class myThread(threading.Thread):
#     def __init__(self, name, link_range):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.link_range = link_range
#
#     def run(self):
#         print("Starting " + self.name)
#         crawler(self.name, self.link_range)
#         print("Ending " + self.name)
#
# def crawler(threadName, link_range):
#     for i in range(link_range[0], link_range[1] + 1):
#         try:
#             r = requests.get(link_list[i], timeout=20)
#             print(threadName, r.status_code, link_list[i])
#         except Exception as e:
#             print(threadName, 'Error:', e)
#
#
# thread_list = []
# link_range_list = [(0, 200), (201, 400), (401, 600), (601, 800), (801, 1000)]
#
# for i in range(1, 6):
#     thread = myThread("Thread-" + str(i), link_range_list[i - 1])
#     thread.start()
#     thread_list.append(thread)
#
# for thread in thread_list:
#     thread.join()
#
# end = time.time()
# print('Tatal time : ', end - start)