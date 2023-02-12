from typing import Optional


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


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(1)
obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# obj.deleteAtIndex(1)
idx2 = obj.get(1)
# obj.addAtHead(1)


#

a = 1

"""
["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
[[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]
"""
