import sys

sys.setrecursionlimit(10**6)

from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
ans = 0


def dfs(v, visited):
    global ans
    ans = max(ans, v)
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, visited)


visited = set()
dfs(0, visited)
print(ans + 1)
