class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root = None

        return root