# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ao

import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


def dfs(v, c):
    global is_bipartite
    for nv in G[v]:
        if colors[nv] == -1:
            colors[nv] = not c
            dfs(nv, not c)
        elif colors[nv] == c:
            is_bipartite = False


is_bipartite = True
colors = [-1] * N
for i in range(N):
    if colors[i] == -1:
        colors[i] == 0
        dfs(i, 0)

print("Yes" if is_bipartite else "No")
