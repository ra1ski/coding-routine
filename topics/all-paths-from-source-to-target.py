from collections import deque
from typing import List

import pytest


class Solution:
    params = [
        ([[1,2],[3],[3],[]], [[0,1,3],[0,2,3]])
    ]

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []

        def backtrack(curr, path):
            # base case
            if curr == target:
                results.append(list(path))
                return

            for nxt in graph[curr]:
                path.append(nxt)
                backtrack(nxt, path)
                path.pop()

        path = deque([0])
        backtrack(0, path)

        return results

@pytest.mark.parametrize('graph, expected', Solution.params)
def test_solution(graph, expected):
    s = Solution()

    assert s.allPathsSourceTarget(graph) == expected