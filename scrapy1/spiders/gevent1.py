"""
    File   : gevent1.py
    Author : msw
    Date   : 2019/9/26 14:32
    Ps     : ...
    gevent + Queue 多协程爬虫总时间 :  243.2996973991394

"""
import gevent
from gevent import monkey
monkey.patch_all()              # 将所有设计 IO 操作的地方做标记.这三句话必须写在最上面
import time
import requests
from gevent.queue import Queue, Empty

link_list = []
with open('uuurls.txt','r') as f:
    file_list = f.readlines()
    for each in file_list:
        link = each.split('\t')[1]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
def crawler(index):
    Process_id = 'Process-' + str(index)
    while not workQueue.empty():
        url = workQueue.get(timeout = 2)
        try:
            r = requests.get(url, timeout = 20)
            print(Process_id, workQueue.qsize(), r.status_code)
        except Exception as ex:
            print(Process_id, workQueue.qsize(), url, 'Error : ', ex)

def boss():
    for url in link_list:
        workQueue.put_nowait(url)

if __name__ == '__main__':
    workQueue = Queue(1000)
    gevent.spawn(boss).join()
    jobs = []
    for i in range(20):
        jobs.append(gevent.spawn(crawler,i))
    gevent.joinall(jobs)

    end = time.time()
    print('gevent + Queue 多协程爬虫总时间 : ',end-start)