import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)


def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    for vv in g[v]:
        dfs(vv)


ans = 0
for i in range(n):
    visited = [False] * n
    dfs(i)
    ans += sum(visited)

print(ans)
