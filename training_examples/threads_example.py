import threading
import time


# TODO: Computations
# async / asyncio
# treading
# multiprocessing

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    time.sleep(0.01)  # very computational many hard so code
    return factorial(n - 1) * n


numbers = [100, 75, 50, 25]

start = time.time()
threads: list[threading.Thread] = []

for num in numbers:
    result = factorial(num)
    print(result)

for num in numbers:
    thread = threading.Thread(target=factorial, args=[num])
    thread.start()
    threads.append(thread)

for th in threads:
    th.join()

end = time.time() - start
print(end)
# single thread -> 2.485s
# 4 threads -> 0.999s (0.62s)
