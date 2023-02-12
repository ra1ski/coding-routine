from collections import deque
from typing import Optional


class Solution:
    # Recursion
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []

        def h(node, level):
            if len(levels) == level:
                levels[level].append([])

            levels.append(node.val)

            if node.left:
                h(node.left, level + 1)

            if node.right:
                h(node.right, level + 1)

        h(root, 0)

        return levels

    # Iteration
    def levelOrderIteration(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        levels, level = [], 0

        while q:
            levels.append([])

            for i in range(len(q)):
                node = q.popleft()

                levels[level].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return levels

