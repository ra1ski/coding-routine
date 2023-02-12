# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree__slicing(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(inorder, postorder):
            """
                inorder = [2,1,4,3,5], postorder = [2,4,5,3,1]
    
                steps:
                - inorder[4,3,5], postorder[2,4,5,3]
                - inorder[5], postorder[2,4,5]
                - inorder[], postorder[2,4]
    
                - inorder[2,1,4,3,5], postorder[2,4]
                - inorder[2,1], postorder[2]
            """
            # base condition
            if not inorder or not postorder:
                return

            root = TreeNode(postorder.pop())
            mid = inorder.index(root.val)

            root.right = helper(inorder[mid + 1:], postorder)
            root.left = helper(inorder[:mid], postorder)

            return root

        return helper(inorder, postorder)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapper = {value:idx for value, idx in enumerate(inorder)}

        def helper(low, high):
            """
If in_left > in_right, the subtree is empty, return None.

Pick the last element in postorder traversal as a root.

Root value has index index in the inorder traversal,
elements from in_left to index - 1 belong to the left subtree,
and elements from index + 1 to in_right belong to the right subtree.

Following the postorder logic, proceed recursively first to construct the right subtree helper(index + 1, in_right) and then to construct the left subtree helper(in_left, index - 1).

Return root.
                inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
                - l,h = 0,4; root = 3, mid = 1 [9,15,7,20,3]
                - l,h = 2,4; root = 20, mid = 3 [9,15,7,20]
                - l,h = 4,4; root = 7, mid = 4 [9,15,7]
                - l,h = 5,4; return
                - l,h = 2,4; root = 20, mid = 3 [9,15]
                - l,h = 2,3; root = 15; mid = 2 [9]
                - l,h = 2,1; return

                - l,h = 0,4; root = 3, mid = 1
                - l,h = 0,0; root = 9; mid = 0
                - l,h = 0,-1; return


                steps:
                - inorder[4,3,5], postorder[2,4,5,3]
                - inorder[5], postorder[2,4,5]
                - inorder[], postorder[2,4]

                - inorder[2,1,4,3,5], postorder[2,4]
                - inorder[2,1], postorder[2]
            """
            # Base condition. Subtree is empty
            if low > high:
                return

            root = TreeNode(postorder.pop())
            mid = mapper[root.val]

            root.right = helper(mid+1, high)
            root.left = helper(low, mid-1)

            return root

        return helper(0, len(inorder) - 1)