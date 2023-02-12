from threading import Lock


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyCircularQueue:

    def __init__(self, k: int):
        self.head, self.tail = None, None
        self.capacity = k
        self.count = 0
        self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        with self.queueLock:
            if self.isFull():
                return False

            node = Node(value)

            if self.isEmpty():
                self.head = node
                self.tail = self.head
            else:
                self.tail.next = node
                self.tail = node

            self.count += 1

            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = self.head.next
        self.count -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.tail.value

    def isEmpty(self) -> bool:
        # or self.count == 0
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.k = k
#         self.q = [0]*k
#         self.count = 0
#         self.head = 0
#         """
#         tail formula:
#         tail = (head + count - 1) % capacity
#         """

#     def enQueue(self, value: int) -> bool:
#         with self.queueLock:
#             if self.isFull():
#                 return False

#             self.q[(self.head + self.count) % self.k] = value
#             self.count +=1

#             return True


#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False

#         self.head = (self.head + 1) % self.k
#         self.count -= 1

#         return True


#     def Front(self) -> int:
#         if self.count == 0:
#             return -1

#         return self.q[self.head]


#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1

#         tail_index = (self.head + self.count - 1) % self.k

#         return self.q[tail_index]

#     def isEmpty(self) -> bool:
#         # or self.count == 0
#         return self.count == 0

#     def isFull(self) -> bool:
#         return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()