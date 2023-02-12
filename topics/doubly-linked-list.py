class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
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
            head = self.head
            head.prev = node
            node.next = head

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            tail = self.head
            node.prev = tail
            tail.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            i = 0

            while current:
                if index == i:
                    break

                current = current.next
                i += 1

            node = Node(val)

            prev = current.prev
            prev.next = node
            node.prev = prev
            node.next = current
            current.prev = node



    def get(self, index: int) -> int:
        if not self.head:
            return -1

        if index == 0:
            return self.head.val

        i = 0
        current = self.head

        while current:
            if index == i:
                return current.val

            current = current.next
            i += 1

        return -1

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return None

        if index == 0 and not self.head.next:
                self.head = None
        else:
            current = self.head
            i = 0

            while current:
                if i == index:
                    break

                current = current.next
                i += 1

            if current.prev:
                prev = current.prev
                prev.next = current.next
                current.prev = prev
            else:
                current.next.prev = None

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# a = obj.get(1)
# obj.deleteAtIndex(1)
b = obj.deleteAtIndex(0)
z = 1
# obj.deleteAtIndex(index)