# N, K = map(int, input().split())
# G = [[] for _ in range(N)]
# for _ in range(N - 1):
#     a, b = map(lambda x: int(x) - 1, input().split())
#     G[a].append(b)
#     G[b].append(a)
# V = set(map(lambda x: int(x) - 1, input().split()))

N, K = 7, 3
G = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
V = [0, 2, 4]


def dfs(u, p):
    global ans
    ok = False
    if u in V:
        ok = True
    for v in G[u]:
        if v != p:
            if dfs(v, u):
                ok = True
    if ok:
        ans += 1
    return ok


ans = 0
dfs(0, -1)
print(ans)
