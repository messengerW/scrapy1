"""
    File   : thread2.py
    Author : msw
    Date   : 2019/9/25 21:04
    Ps     : 第二个实例，较上一个例子有所改进：上一个例子中每个爬虫负责200个url，当某个线程率先完成任务后就会退出
             线程，然而其他线程仍在工作。针对于这一点，我们使用Python的Queue，每个线程动态的从Queue中获取url，
             然后爬取，直至爬完1000个url。
    Tatal time :  396

"""
import time
import requests
import threading
import queue as Queue

link_list = []

with open('uuurls.txt','r') as file:
    file_list = file.readlines()
    for each in file_list:
        link = each.split('\t')[1]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
class myThread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                crawler(self.name, self.q)
            except:
                break
        print("Ending " + self.name)

def crawler(threadName, q):
    url = q.get(timeout = 2)
    try:
        r = requests.get(url,timeout = 20)
        print(q.qsize(), threadName, r.status_code, url)
    except Exception as ex:
        print(q.qsize(), threadName, url, 'Error: ', ex)

thread_list = ["Thread-1","Thread-2","Thread-3","Thread-4","Thread-5"]
workQueue = Queue.Queue(1000)
threads = []

for tname in thread_list:
    thread = myThread(tname, workQueue)
    thread.start()
    threads.append(thread)

for url in link_list:
    workQueue.put(url)

for t in threads:
    t.join()

end = time.time()
print('Total time : ', end-start)
print("Exittttttttttttttttt")
