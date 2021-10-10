# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = None
        fast = head

        while n > 0:
            if not fast or not fast.next:
                return head.next
            fast = fast.next
            n -= 1

        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
