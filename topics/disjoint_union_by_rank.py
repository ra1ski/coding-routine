# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size # height

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        print(x, y)
        if rootX != rootY:
            # print(x,y,rootX,rootY,self.rank[rootX], self.rank[rootY])
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
print(uf.root)
print(uf.rank)
uf.union(1, 2)
print(uf.root)
print(uf.rank)
uf.union(2, 5)
print(uf.root)
print(uf.rank)
uf.union(1, 3)
print(uf.root)
print(uf.rank)
# uf.union(6, 7)
# print(uf.root)
# print(uf.rank)
# uf.union(3, 8)
# print(uf.root)
# print(uf.rank)
# uf.union(8, 9)
# print(uf.root)
# print(uf.rank)
# print(uf.connected(1, 5))  # true
# print(uf.connected(5, 7))  # true
# print(uf.connected(4, 9))  # false
# # 1-2-5-6-7 3-8-9-4
# uf.union(9, 4)
# print(uf.connected(4, 9))  # true