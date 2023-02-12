"""
- separate memory space
- one gil
-
"""
import os
import time
from multiprocessing import Process, Value, Array, Lock


# def add_100(number: int, lock):
#     for i in range(100):
#         time.sleep(0.01)
#
#         # prevent race condition
#         with lock:
#             number.value += 1

def add_100(numbers: list, lock):
    for i in range(100):
        time.sleep(0.01)

        # prevent race condition
        with lock:
            for i in range(len(numbers)):
                numbers[i] += 1


if __name__ == '__main__':
    lock = Lock()
    # shared = Value('i', 0)
    shared = Array('d', [0.0, 100.0, 200.0])
    # print('At beginning: ', shared.value)
    print('At beginning: ', shared[:])

    p1 = Process(target=add_100, args=(shared, lock))
    p2 = Process(target=add_100, args=(shared, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('At end: ', shared[:])
    # print('At end: ', shared.value)

# def square():
#     for i in range(100):
#         result = i * i
#         time.sleep(0.1)
#
#
# processes = []
# num_processes = os.cpu_count()
#
# for i in range(num_processes):
#     p = Process(target=square)
#     processes.append(p)
#
# for process in processes:
#     process.start()
#
# for process in processes:
#     process.join()
#
# print('end')
