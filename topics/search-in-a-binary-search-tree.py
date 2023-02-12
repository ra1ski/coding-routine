# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST__recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == val:
            return root

        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


    def searchBST__iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == val:
            return root

        while root:
            if root.val == val:
                return root

            if val > root.val:
                root = root.right
            else:
                root = root.left

        return False

    def searchBST__iterative2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            if val > root.val:
                root = root.right
            else:
                root = root.left

        return root
