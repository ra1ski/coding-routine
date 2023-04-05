## Lists ##
- a["a","b","c","d","e","f"]
- a[:3] - from zero until 3 (without three)
- a[2:] - from two till the end
- a[1:5] - from one until 5
- a[3:4] - third element.

## Trees ##

DFS - use stack
BFS (level order) - use queue

List slicing [start:end] - start includes itself, until the end - doesn't include end
----
* Patterns *
- Если нужно сравнить суммы слева и справа - это prefix sum (https://leetcode.com/problems/find-pivot-index)

----

1. We care only about worst case
2. Drop constants
3. n+n (a+b) - 2 separate for loops for instance
(a*b) - two different loops in one another
4. drop non dominant O(n + n^2) = O(n^2)

O(n^2) - squared, quadratic time

-- --
Understand tradeoffs, how to solve problems.
The interview isn't about your ability to memorize data structures and algorithms, most people
make that mistake and interviewers can detect right away who actually knows these things versus just
memorizing them the week before the interview.

What do they search?
1. Analytical
2. Coding
3. Technical
4. Communication
skills


- Can we assume always 2 parameters?

- def func(arr1, arr2): - if you make a hash from arr1, then space complexity is O(a), not O(n)

-- Hash tables --
    search O(1)
    insert O(1)
    lookup O(1)
    delete O(1)

pros
fast lookups
fast insertions
flexible keys

cons
unordered
slow key iteration

Notes:
- Note: to create an empty set you have to use set(), not {}


https://leetcode.com/problems/merge-sorted-array/solution/
Interview Tip: Whenever you're trying to solve an array problem in-place, always consider the possibility of iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot easier.


### Techniques

## Two sums
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
https://leetcode.com/problems/squares-of-a-sorted-array/

---
Two pointers
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1156/
- And it is worth noting that this technique is often used in a sorted array.

Two pointers in LL template
// Initialize slow & fast pointers
ListNode* slow = head;
ListNode* fast = head;
/**
 * Change this condition to fit specific problem.
 * Attention: remember to avoid null-pointer error
 **/
while (slow && fast && fast->next) {
    slow = slow->next;          // move slow pointer one step each time
    fast = fast->next->next;    // move fast pointer two steps each time
    if (slow == fast) {         // change this condition to fit specific problem
        return true;
    }
}
return false;   // change return value to fit specific problem

One Pass
https://leetcode.com/problems/max-consecutive-ones/solution/

---
Binary Tree
---

DAG - Directed acyclic Graph

- PreOrder - Root, Left, Right

- InOrder - Left, Root, Right
Left element from the root in array is a left node.

- PostOrder - Left, Right, Root
The root is the last element in array

Two general strategies to traverse a tree:
- Breadth First Search (BFS)

- Depth First Search (DFS)
# Iterations
- use stack, put root node as a first element
# Recursion

To be cautious, the complexity might be different due to a different implementation.
It is comparatively easy to do traversal recursively but when the depth of the tree is too large,
we might suffer from stack overflow problem.
That's one of the main reasons why we want to solve this problem iteratively sometimes.

# Postorder
Need 2 stacks. Fill 1st, and traverse the second


---
Graphs
- Cyclic
- Asyclic
- Weighted
- Unweighted
- Directed
- Undirected

DAG Directed Asyclic Graph

elge_list_graph = [[0,2],[2,3], [2,1], [1,3]]
adjacent_list_graph = [[2], [2,3], [0,1,2], [1,2]]
adjacent_matrix = [
    [0,0,1,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,1,0],
]

---
Recusion

Each time a recursive function calls itself, it reduces the given problem into subproblems.
The recursion call continues until it reaches a point where the subproblem can be solved without further recursion.

https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/1669/


---
Stacks and Queues

Use queue for BFS


Queue - FIFO
Enque to back, deque to front

---------------------
Algorithms
---------------------
 ------------
| 7. Tree BFS |
 ------------
This pattern is based on the Breadth First Search (BFS) technique to traverse a tree and uses a queue to keep track of all the nodes of a level before jumping onto the next level. Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach.
The Tree BFS pattern works by pushing the root node to the queue and then continually iterating until the queue is empty. For each iteration, we remove the node at the head of the queue and “visit” that node. After removing each node from the queue, we also insert all of its children into the queue.

How to identify the Tree BFS pattern:
If you’re asked to traverse a tree in a level-by-level fashion (or level order traversal)
Problems featuring Tree BFS pattern:

Binary Tree Level Order Traversal (easy)
Zigzag Traversal (medium)

