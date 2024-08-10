# https://atcoder.jp/contests/abc126/tasks/abc126_d

import sys

sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N)]
W = {}
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    W[(u, v)] = w
    W[(v, u)] = w


def dfs(v, c):
    for nv in G[v]:
        if colors[nv] == -1:
            nv_c = -1
            if W[(v, nv)] % 2 == 0:
                nv_c = c
            else:
                nv_c = 0 if c else 1
            colors[nv] = nv_c
            dfs(nv, nv_c)


colors = [-1] * N
colors[0] = 0
dfs(0, 0)

print(*colors)
