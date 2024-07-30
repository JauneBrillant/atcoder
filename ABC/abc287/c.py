import sys

sys.setrecursionlimit(10**6)

from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
visited = [False] * n


def f(p, v):
    visited[v] = True
    if len(g[v]) > 2:
        return False

    for vv in g[v]:
        if vv == p:
            continue
        if visited[vv]:
            return False
        if not f(v, vv):
            return False
    return True


print("Yes" if f(-1, 0) and all(visited) else "No")
