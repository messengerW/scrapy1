"""
    File   : gevent_douban.py
    Author : msw
    Date   : 2019/9/26 15:22
    Ps     : 协程好强啊。拿豆瓣这个小白鼠试一下...
    
"""
import gevent.monkey
gevent.monkey.patch_all()
from gevent.pool import Pool
import requests
import time
from queue import Queue

link_list = []
url = 'https://movie.douban.com/top250'
link_list.append(url)
for i in range(1,10):
    ppp = '?start=' + str(25*i)
    link = url + ppp
    link_list.append(link)


start = time.time()
def crawler(index):
    process_id = 'Process-' + str(index)
    while not workQueue.empty():
        url = workQueue.get(timeout=1)
        try:
            r = requests.get(url, timeout = 3)
            print(process_id, workQueue.qsize(), r.status_code, url)
        except Exception as ex:
            print(process_id, workQueue.qsize(), url, 'Error : ', ex)


def boss():
    for url in link_list:
        workQueue.put_nowait(url)


if __name__ == '__main__':
    workQueue = Queue(10)
    gevent.spawn(boss).join()
    jobs = []
    for i in range(10):
        jobs.append(gevent.spawn(crawler,i))
    gevent.joinall(jobs)

    end = time.time()
    print('Total time : ',end-start)