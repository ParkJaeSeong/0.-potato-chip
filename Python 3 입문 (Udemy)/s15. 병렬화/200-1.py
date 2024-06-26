# from multiprocessing import (
#     Process,
#     Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
#     Value, Array, Pipe, Manager)

# Jupyter notebook에서는 안됨

import logging
import threading
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')
#     level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(d, lock):
    with lock: 
        i = d['x']
        time.sleep(2)
        d['x'] = i + 1
    logging.debug(d)

def worker2(d, lock):
    with lock: 
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
    logging.debug(d)
    
if __name__ == '__main__':
    d = {'x' : 0 }
    lock = threading.Lock() 
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock)) 
#     lock = multiprocessing.Lock()
#     t1 = multiprocessing.Process(target=worker1, args=(d, lock))
#     t2 = multiprocessing.Process(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logging.debug(d)

