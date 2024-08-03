from collections import defaultdict

import sys

sys.setrecursionlimit(10**6)

n, x, y = map(int, input().split())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
path = []


def dfs(v, visited):
    path.append(v)
    visited.add(v)
    if v == y:
        print(*path)
        return

    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    path.pop()


visited = set()
dfs(x, visited)
