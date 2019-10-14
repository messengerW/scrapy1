"""
    File   : process2.py
    Author : msw
    Date   : 2019/9/26 12:23
    Ps     : Pool + Queue
    Pool + Queue 总时间 :  263.1372985839844

"""
import time
import requests
from multiprocessing import Pool, Manager

link_list = []
with open('uuurls.txt','r') as f:
    file_list = f.readlines()
    for each in file_list:
        link = each.split('\t')[1]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
def crawler(q, index):
    Precess_id = 'Process-' + str(index)
    while not q.empty():
        url = q.get(timeout = 2)
        try:
            r = requests.get(url, timeout = 20)
            print(Precess_id, q.qsize(), r.status_code, url)
        except Exception as ex:
            print(Precess_id, q.qsize(), url, 'Error : ', ex)

if __name__ == '__main__':
    manager = Manager()
    workQueue = manager.Queue(1000)

    for url in link_list:
        workQueue.put(url)
    pool = Pool(processes=8)
    for i in range(9):
        pool.apply_async(crawler, args=(workQueue,i))

    print("Start processes")
    pool.close()
    pool.join()

    end = time.time()
    print('Pool + Queue 总时间 : ', end-start)