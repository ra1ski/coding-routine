from typing import Optional

import pytest


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def addAtHead(self, val: int) -> None:
        node = Node(val)

        if not self.head:
            self.head = node
        else:
            current = self.head
            node.next = current
            self.head = node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            node = Node(val)

            prev = self.traverse_to_index(index - 1)

            if prev:
                current = prev.next
                node.next = current
                prev.next = node

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        current = self.traverse_to_index(index)

        if current:
            return current.val

        return -1

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return None

        if index == 0:
            if not self.head.next:
                self.head = None
            else:
                current = self.head.next
                self.head = current
        else:
            if self.head.next:
                prev = self.traverse_to_index(index - 1)
                if prev and prev.next:
                    current = prev.next
                    prev.next = current.next

    def traverse_to_index(self, index):
        i = 0
        current = self.head

        while current:
            if i == index:
                return current

            i += 1
            current = current.next

        return None


class Solution:
    params = []

    def rotateRight(self, head: Optional[Node], k: int) -> Optional[Node\
        old_tail.next = head

        new_tail = head

        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        new_tail.next = None

        return new_head


ll = MyLinkedList()

ll.addAtTail(1)
ll.addAtTail(2)
ll.addAtTail(3)
ll.addAtTail(4)
ll.addAtTail(5)

s = Solution()

result = s.rotateRight(ll.head, 2)
