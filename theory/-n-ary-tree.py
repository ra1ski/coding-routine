"""
- a binary tree is a special form of a N-ary tree
"""
# Preorder
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.val)

            if node.children:
                stack.extend(node.children[::-1])

        return output


# Postorder
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.val)

            if node.children:
                stack.extend(node.children)

        return output[::-1]

# Level order
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)

            result.append(level)

        return result