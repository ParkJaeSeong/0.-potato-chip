# from multiprocessing import (
#     Process,
#     Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
#     Value, Array, Pipe, Manager)

# Jupyter notebook에서는 안됨

import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i *2

if __name__ == '__main__':
#    t1 = multiprocessing.Process(target=worker1, args=(i,))
    with multiprocessing.Pool(3) as p :
#         r = p.map(worker1, [100, 200])
#         logging.debug('executed')
#         logging.debug(r)

#         r = p.map_async(worker1, [100, 200])
#         logging.debug('executed')
#         logging.debug(r.get(timeout=1))

#         r = p.imap(worker1, [100, 200])
#         logging.debug('executed')
#         logging.debug([i for i in r])

        r = p.imap(worker1, [100, 200])
        logging.debug('executed')
        for i in r:
            logging.debug(i)

        