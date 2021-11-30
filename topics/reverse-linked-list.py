# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, nxt, current = None, None, head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
