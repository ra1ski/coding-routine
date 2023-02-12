# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, output = [root, ], []

        while stack:
            root = stack.pop()
            output.append(root.val)

            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)

        return output

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        def dfs(root):
            if not root:
                return None

            result.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return result