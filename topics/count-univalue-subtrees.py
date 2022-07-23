# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        """
        Base cases:
        - leaf node
        - all children are univalues and have the same value as parent's
        """
        if not root:
            return 0

        self.count = 0

        self.is_uni(root)

        return self.count

    def is_uni(self, root):
        # first base case
        if not root.left and not root.right:
            self.count += 1
            return True

        # check if left and right are both univalues and equal to parent
        # by default let's consider current parent node as univalue
        is_uni = True

        if root.left:
            is_uni = self.is_uni(root.left) and root.val == root.left.val

        if root.right:
            # plus check if the left sibling is univalue
            is_uni = self.is_uni(root.right) and root.val == root.right.val and is_uni

        # second base case is True, add +1
        if is_uni:
            self.count += 1
        # self.count += is_uni

        return is_uni
