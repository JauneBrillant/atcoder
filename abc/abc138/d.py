import sys
import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=-1")

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
nodes = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, p):
    if p != -1:
        nodes[v] += nodes[p]

    for ch in graph[v]:
        if ch != p:
            dfs(ch, v)


for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1

    nodes[p] += x

dfs(0, -1)

print(*nodes)
