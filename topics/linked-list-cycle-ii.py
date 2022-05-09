# https://leetcode.com/problems/linked-list-cycle-ii/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        slow, fast, has_cycle = head, head, False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break

        if has_cycle:
            while head != fast:
                head = head.next
                fast = fast.next

            return head

    def detectCycle2(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        nodes = set()
        current = head

        while current:
            if current in nodes:
                return current
            else:
                nodes.add(current)
                current = current.next