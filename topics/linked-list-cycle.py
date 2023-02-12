# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        current = head

        while current:
            if current in nodes:
                return True
            else:
                nodes.add(current)
                current = current.next

        return False

    def hasCycle0(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow, fast = head, head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

    def hasCycle3(self, head: Optional[ListNode]) -> bool:
        current = head

        while current:
            if current.val == '_':
                return True
            else:
                current.val = '_'
                current = current.next

        return False
