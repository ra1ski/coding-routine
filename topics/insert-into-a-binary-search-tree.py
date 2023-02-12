# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST__recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def insertIntoBST__iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        new_node = TreeNode(val)

        while node:
            if val > node.val:
                if node.righ:
                    node = node.right
                else:
                    node.right = new_node
                    return root
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    return root

        return new_node