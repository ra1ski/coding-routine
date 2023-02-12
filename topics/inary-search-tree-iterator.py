# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class BSTIterator:
#
#     def __init__(self, root: Optional[TreeNode]):
#         self.index = -1
#         self.flattened_bst = []
#         self.flatten_bst(root)
#
#     def flatten_bst(self, root):
#         if not root:
#             return
#
#         self.flatten_bst(root.left)
#         self.flattened_bst.append(root.val)
#         self.flatten_bst(root.right)
#
#     def next(self) -> int:
#         self.index += 1
#         return self.flattened_bst[self.index]
#
#     def hasNext(self) -> bool:
#         return self.index + 1 < len(self.flattened_bst)


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        topmost_node = self.stack.pop()

        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
