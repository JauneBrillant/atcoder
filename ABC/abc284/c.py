import sys

sys.setrecursionlimit(10**7)
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def solve():
    cnt = 0
    visited = [False] * n

    def dfs(curr_v):
        visited[curr_v] = True
        for neighbor_v in graph[curr_v]:
            if not visited[neighbor_v]:
                dfs(neighbor_v)

    for v in range(n):
        if not visited[v]:
            dfs(v)
            cnt += 1

    return cnt


ans = solve()
print(ans)
