# https://leetcode.com/problems/validate-binary-search-tree/
"""
- recursive: track low and high
- iterative: track low n high in stack

- inorder recursive: track prev
- inorder iterative
"""
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def validate(node: TreeNode, low=-math.inf, high=math.inf) -> bool:
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)

    def isValidBST__iterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, low, high = stack.pop()

            if not node:
                continue

            if node.val <= low or node.val >= high:
                return False

            stack.append((node.right, node.val, high))
            stack.append((node.left, low, node.val))

        return True

    def isValidBST__inroder_recursive(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def validate(node: TreeNode) -> bool:
            if not node:
                return True

            if not validate(node.left):
                return False

            if node.val <= self.prev:
                return False

            self.prev = node.val

            return validate(node.right)

        self.prev = -math.inf

        return validate(root)
