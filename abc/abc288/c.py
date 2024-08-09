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


def dfs(v, visited):
    component_cnt = 1
    edge_cnt = 0
    visited.add(v)

    for nv in G[v]:
        edge_cnt += 1
        if nv not in visited:
            sub_com, sub_edge = dfs(nv, visited)
            component_cnt += sub_com
            edge_cnt += sub_edge

    return component_cnt, edge_cnt


ans = 0
visited = set()
for i in range(N):
    if i not in visited:
        component_cnt, edge_cnt = dfs(i, visited)
        ans += (edge_cnt // 2) - (component_cnt - 1)

print(ans)
