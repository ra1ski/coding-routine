# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1,2,3,4,5
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head

        while n > 0:
            if not fast or not fast.next:
                return head.next

            fast = fast.next
            n -= 1

        slow = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return head