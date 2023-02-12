"""
- Good for searching, comparing
- O (log n)

to the right - constantly increases
to the left - decreases

Like a normal binary tree, we can traverse a BST in preorder, inorder, postorder or level-order.
However, it is noteworthy that inorder traversal in BST will be i   n ascending order.
Therefore, the inorder traversal is the most frequent used traversal method of a BST.

The strength of a BST is that you can perform all search, insertion and deletion operations in O(h) time complexity even in the worst case.

Usually, if you want to store data in order and need several operations, such as search, insertion or deletion, at the same time, a BST might be a good choice.
"""

# Binary tree properties
"""
- Perfect binary tree. 
1) The number of nodes on each level doubles as we move down
2) The nums of nodes of the last level is equal to sum of all nodes +1, it means that last node contains the half of all nodes 
"""

# O(log n)
"""
- The log of nodes == height of tree
"""

# Balanced n unbalanced ST
"""
- Unbalanced is O(n)

AVL trees and Red/Black trees are for balancing trees.
"""


"""
Problem: Design a class to find the kth largest element in a stream.

A most obvious way to solve this problem is to sort the array in descending order first and then return the kth element in the array.

But we have to sort for the new element everytime when we insert a new value in order to perform the search operation in O(1) time complexity. But the time complexity of the insertion operation will be O(N) in average. Therefore, time complexity will be O(N^2) in total
"""

"""
Successor = "after node", i.e. the next node, or the smallest node after the current one.
To find a successor, go to the right once and then as many times to the left as you could.

Predecessor = "before node", i.e. the previous node, or the largest node before the current one.
To find a predecessor, go to the left once and then as many times to the right as you could.


"""