import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

# N, M = 6, 7
# G = [[] for _ in range(N)]
# EDGES = [(1, 6), (2, 6), (3, 6), (2, 4), (3, 5), (1, 3), (1, 4)]
# for u, v in EDGES:
#     u -= 1
#     v -= 1
#     G[u].append(v)
#     G[v].append(u)


def is_bipartite():
    def dfs(v, c):
        colors[v] = c
        for nv in G[v]:
            if colors[nv] == -1:
                if not dfs(nv, not c):
                    return False
            elif colors[nv] == c:
                return False
        return True

    colors = [-1] * N
    for i in range(N):
        if colors[i] == -1:
            if not dfs(i, 0):
                return False
    return True


print("Yes" if is_bipartite() else "No")
