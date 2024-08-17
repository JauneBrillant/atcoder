from atcoder.dsu import DSU

N = int(input())
edges = list(tuple(map(int, input().split())) for _ in range(N - 1))
edges.sort(key=lambda x: x[2])

dsu = DSU(N)
ans = 0
for u, v, w in edges:
    u -= 1
    v -= 1
    ans += w * dsu.size(u) * dsu.size(v)
    dsu.merge(u, v)
print(ans)
