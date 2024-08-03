import sys

sys.setrecursionlimit(10**7)
from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(curr_v, visited):
    visited.add(curr_v)
    highest = curr_v
    for v in graph[curr_v]:
        if v in visited:
            continue
        highest = max(highest, dfs(v, visited))
    return highest


visited = set()
print(dfs(1, visited))
