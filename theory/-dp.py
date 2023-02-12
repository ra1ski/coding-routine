"""
Dynamic programming is a powerful tool because it can break a complex problem into manageable subproblems,
avoid unnecessary recalculation of overlapping subproblems, and use the results of those subproblems
to solve the initial complex problem.

There are two ways to implement a DP algorithm:

Bottom-up, also known as tabulation.
Top-down, also known as memoization.


--- Top-down ---
memoizing a result means to store the result of a function call, usually in a hashmap or an array, so that when
the same function call is made again, we can simply return the memoized result instead of recalculating the result.

memoization means caching results from function calls and then referring to those results in the future instead of recalculating them. This is usually done with a hashmap or an array.

We'll be talking more about these two options throughout the card.
For now, all you need to know is that top-down uses recursion, and bottom-up uses iteration.


1 The problem can be broken down into "overlapping subproblems" - smaller versions of the original problem that are re-used multiple times
2 The problem has an "optimal substructure" - an optimal solution can be formed from optimal solutions to the overlapping subproblems of the original problem

The first characteristic that is common in DP problems is that the problem will ask for the optimum value (maximum or minimum) of something, or the number of ways there are to do something. For example:

What is the minimum cost of doing...
What is the maximum profit from...
How many ways are there to do...
What is the longest possible...
Is it possible to reach a certain point...


The second characteristic that is common in DP problems is that future "decisions" depend on earlier decisions. Deciding to do something at one step may affect the ability to do something in a later step. This characteristic is what makes a greedy algorithm invalid for a DP problem - we need to factor in results from previous decisions.
"""

"""
With DP problems, we can use logical thinking to find the answer to the original problem for certain inputs, in this case we reason that there is 1 way to climb to the first stair and 2 ways to climb to the second stair. We can then use a recurrence relation to find the answer to the original problem for any state, in this case for any stair number. Finding the recurrence relation involves thinking about how moving from one state to another changes the answer to the problem.

In this article, we will be looking at the House Robber problem. In an earlier section of this explore card, we talked about how House Robber fits the characteristics of a DP problem. It's asking for the maximum of something, and our current decisions will affect which options are available for our future decisions. Let's see how we can use the framework to develop an algorithm for this problem.
You may be wondering - why don't we include a state variable that is a boolean indicating if we robbed the previous house or not? We certainly could include this state variable, but we can develop our recurrence relation in a way that makes it unnecessary.
"""