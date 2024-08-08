import threading
import time
from queue import Queue
import multiprocessing as multi

# TODO: Computations
# async / asyncio
# treading, when task is i/o bound threading is great
# (request url, read file from file/os, read from DB)

# but if you have hard maths / calculations / processing of DATA threading is
# not good.

# multiprocessing
# to get use of multiple cores, we have to use multiprocessing library.


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    time.sleep(0.01)  # very computational many hard so code
    return factorial(n - 1) * n

def do_smth(n: int, queue: Queue):
    result = 1
    while n > 0:
        out = out * n
        n -= 1
    time.sleep(0.01)  # very computational many hard so code
    queue.put(result)

def do_something(n: int, results: list[int], lock: threading.Lock):
    result = 1
    while n > 0:
        result = result * n
        n -= 1
    time.sleep(0.01)  # very computational many hard so code
    lock.acquire()
    results.append(result)
    lock.release()

files = [] # split input to 4 and assing each piece to a thread.

# FIFO first in first out.
# x = []
# x.append(5)
# x.append(6)
# x.get -> 5, x = [6], we will use que to give results back to main thread
# (the htread that runs program)
q = Queue(maxsize=10)


numbers = [100, 75, 50, 25]

start = time.time()
threads: list[multi.Process] = []

for num in numbers:
    result = factorial(num)
    print(result)

for num in numbers:
    thread = multi.Process(target=do_something(), args=[num, results, 1])
    thread.start()
    threads.append(thread)

for th in threads:
    th.join()



# while not q.empty():
#     val = q.get()
#     print(val)


end = time.time() - start
print(end)
# single thread -> 2.485s
# 4 threads -> 0.999s (0.62s)
