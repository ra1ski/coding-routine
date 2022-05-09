# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1,2,3,4,5
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        fast = head

        while n > 0:
            if not fast.next:
                return head.next

            n -= 1
            fast = fast.next

        slow = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return head

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0

        dummy = ListNode(0)
        first = head
        dummy.next = head

        while first:
            first = first.next
            i += 1

        prev_index = i - n
        first = dummy

        while prev_index > 0:
            prev_index -= 1
            first = first.next

        first.next = first.next.next

        return dummy.next
