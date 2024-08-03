import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)


n, x, y = map(int, input().split())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v, target, visited, path):
    path.append(v)
    visited.add(v)
    if v == target:
        return path
    for neighbor in graph[v]:
        if neighbor not in visited:
            res = dfs(neighbor, target, visited, path)
            if res != None:
                return res
    path.pop()
    return None


visited = set()
ans = dfs(x, y, visited, path=[])
print(*ans)
