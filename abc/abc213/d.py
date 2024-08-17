N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)


def dfs(u, visited, path):
    visited[u] = True
    path.append(u + 1)

    for v in sorted(G[u]):
        if not visited[v]:
            dfs(v, visited, path)
            path.append(u + 1)
    return path


ans = dfs(0, [False] * N, [])
print(*ans)
