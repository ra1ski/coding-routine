"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth__traversal(self, root: 'Node') -> int:
        if not root:
            return 0

        stack = [(1, root)]
        depth = 0

        while stack:
            current_depth, node = stack.pop()
            depth = max(current_depth, depth)

            if node.children:
                for child in node.children:
                    stack.append((current_depth + 1, child))

        return depth

    def maxDepth__recursion(self, root: 'Node') -> int:
        if not root:
            return 0

        if root.children:
            heights = [self.maxDepth__recursion(child) for child in root.chidlren]

            return max(heights) + 1
        else:
            return 1