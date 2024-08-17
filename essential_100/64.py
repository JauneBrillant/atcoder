class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_y] = root_x


def kruskal(n, edges):
    dsu = UnionFind(n)
    edges.sort(key=lambda x: x[2])

    mst_weight = 0
    mst_edges = []

    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.unite(u, v)
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight


N, M = map(int, input().split())
edges = list(tuple(map(int, input().split())) for _ in range(M))
mst_weight = kruskal(N, edges)
print(mst_weight)
