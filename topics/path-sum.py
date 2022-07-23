# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum__recursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    def hasPathSum__iterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            node, current_sum = stack.pop()

            if not node.left and not node.right and current_sum == 0:
                return True

            if node.left:
                stack.append((node.left, current_sum - node.left.val))

            if node.right:
                stack.append((node.right, current_sum - node.right.val))

        return False