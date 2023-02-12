# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric__recursive(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            return (node1.val == node2.val) and is_mirror(node1.left, node2.right) and is_mirror(node2.left,
                                                                                                 node1.right)

        return is_mirror(root, root)

    def isSymmetric__iterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        q = collections.deque([root, root])

        while q:
            l = q.popleft()
            r = q.popleft()

            if not l and not r:
                continue

            if not l or not r:
                return False

            if r.val != l.val:
                return False

            q.extend([l.left, r.right, l.right, r.left])
            # which equals to
            # q.append(l.left)
            # q.append(r.right)
            # q.append(l.right)
            # q.append(r.left)            

        return True