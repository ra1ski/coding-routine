"""
- entity within process
- great for IO-bound
- starts fast

- limiteg by gil
- no effect for CPU-bound tasks
- not interrupteable
- race condition?

GIL - global interpreter lock
- one thread at a time to excecute
- memory management in CPython is not thread-safe
"""

# import time
# from threading import Thread
#
#
# def square():
#     for i in range(20):
#         result = i * i
#         time.sleep(0.1)
#
#
# threads = []
# num_threads= 10
#
# for i in range(num_threads):
#     t = Thread(target=square)
#     threads.append(t)
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print('end')


# Race condition
from threading import Thread, Lock
import time

value = 0


def increase(lock):
    global value

    # lock.acquire()
    with lock:
        local_value = value
        local_value += 1
        time.sleep(0.1)
        value = local_value

    # lock.release()


if __name__ == '__main__':
    print('Value - ', value)
    lock = Lock()

    threads = []

    for _ in range(3):
        threads.append(Thread(target=increase, args=(lock,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    # thread1 = Thread(target=increase, args=(lock,))
    # thread2 = Thread(target=increase, args=(lock,))
    #
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()

    print('Value end - ', value)
