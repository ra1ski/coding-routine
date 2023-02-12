from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque([], size)

    def next(self, val: int) -> float:
        # size, queue = self.size, self.queue
        self.queue.append(val)

        return sum(self.queue) / len(self.queue)