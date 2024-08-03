import sys
import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=-1")

n, x, y = map(int, input().split())
x -= 1
y -= 1

graph = [[] for _ in range(n)]
path = []

for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def dfs(parent, curr_v):
    path.append(curr_v + 1)
    if curr_v == y:
        exit(print(*path))

    for v in graph[curr_v]:
        if parent != v:
            dfs(curr_v, v)

    path.pop()


dfs(-1, x)
