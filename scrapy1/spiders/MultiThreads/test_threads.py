# """
#     File   : _thread.py
#     Author : msw
#     Date   : 2019/9/23 22:59
#     Ps     : ...
#
# """
# import time
# import threading
#
# class myThread(threading.Thread):
#     def __init__(self,name,delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#     def run(self):
#         print("Starting " + self.name)
#         print_time(self.name, self.delay)
#         print("Ending " + self.name)
#
# def print_time(ThreadName, delay):
#     count = 0
#     while count < 3:
#         time.sleep(delay)
#         print(ThreadName,time.ctime())
#         count += 1
#
# threads = []
#
# thread1 = myThread("thread-1",1)
# thread2 = myThread("thread-2",2)
#
# thread1.start()
# thread2.start()
#
# threads.append(thread1)
# threads.append(thread2)
#
# for th in threads:
#     th.join()
#
# print("Exiting Main Thread")