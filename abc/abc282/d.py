import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)


def solve(v, c):
    def dfs(v, c):
        nonlocal a, b, edge, is_bipartite
        colors[v] = c
        if c:
            a += 1
        else:
            b += 1

        for nv in G[v]:
            edge += 1
            if colors[nv] == -1:
                dfs(nv, not c)
            elif colors[nv] == c:
                is_bipartite = False

    a, b, edge = 0, 0, 0
    is_bipartite = True

    dfs(v, c)

    if is_bipartite:
        return a * b - edge // 2
    else:
        return 0


ans = 0
colors = [-1] * N
for i in range(N):
    if colors[i] == -1:
        ans += solve(i, 0)

print(ans)
