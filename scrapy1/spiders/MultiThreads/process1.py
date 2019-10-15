# """
#     File   : process1.py
#     Author : msw
#     Date   : 2019/9/26 11:48
#     Ps     : Python 多线程爬虫只能运行在单核上，各个线程以并发的方法异步运行，无法发挥多核CPU的资源。
#              而多进程爬虫则可以利用CPU的多核，进程数取决于CPU个数。
#     Process +  Queue 多进程爬虫总时间 :  1622.6315760612488
# """
# import time
# import requests
# from multiprocessing import cpu_count, Process, Queue
#
# link_list = []
# with open('uuurls.txt','r') as f:
#     file_list = f.readlines()
#     for each in file_list:
#         link = each.split('\t')[1]
#         link = link.replace('\n','')
#         link_list.append(link)
#
# start = time.time()
# class MyProcess(Process):
#     def __init__(self, q):
#         Process.__init__(self)
#         self.q = q
#     def run(self):
#         while not self.q.empty():
#             crawler(self.q)
#         print("Ending ", self.pid)
#
# def crawler(q):
#     url = q.get(timeout = 2)
#     try:
#         r = requests.get(url,timeout = 20)
#         print(q.qsize(), r.status_code, url)
#     except Exception as ex:
#         print(q.qsize(), url, 'Error: ', ex)
#
# if __name__ == '__main__':
#     ProcessNames = ["Process-1","Process-2","Process-3","Process-4",
#                     "Process-5","Process-6","Process-7","Process-8"]
#     workQueue = Queue(1000)
#
#     for url in link_list:
#         workQueue.put(url)
#
#     for i in range(0,8):
#         pro = MyProcess(workQueue)
#         pro.daemon = True
#         pro.start()
#         pro.join()
#
#     end = time.time()
#     print('Process +  Queue 多进程爬虫总时间 : ', end-start)
#     print("The CPU number is : %d" % cpu_count())
#
#
#
#
