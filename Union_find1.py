# Union findクラスの実装
class UnionFind:
    # インスタンス化
    def __init__(self, size):
        # リスト内包表記
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# テスト
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))
print(uf.connected(5, 7))
print(uf.connected(4, 9))
uf.union(9, 4)
print(uf.connected(4, 9))
