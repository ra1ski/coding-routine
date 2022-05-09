# https://leetcode.com/problems/middle-of-the-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next

            slow = slow.next

        return slow

#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head

#         current, middle = head, head
#         i = 1

#         while current and current.next:
#             current = current.next

#             if i % 2 == 0:
#                 middle = middle.next

#             i += 1

#         if i % 2 == 0:
#             return middle.next

#         return middle

    def middleNode3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]