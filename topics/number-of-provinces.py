from typing import List


class UnionSet:
    def __init__(self, size):
        self.root = list(range(size))

    def find(self, x) -> int:
        while x != self.root[x]:
            x = self.root[x]

        return x

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        m_len = len(isConnected)
        uf = UnionSet(m_len)
        for r in range(m_len):
            for c in range(r, m_len):
                if isConnected[r][c] == 1:
                    uf.union(r, c)

        return len(set(uf.root))

s = Solution()

c = s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
# c = s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
a = 1
# print(c)