N, M = map(int, input().split())
edges = list(tuple(map(int, input().split())) for _ in range(M))


def floyd_warshall():
    INF = float("inf")
    dist = [[0 if i == j else INF for j in range(N)] for i in range(N)]

    for u, v, t in edges:
        dist[u - 1][v - 1] = t
        dist[v - 1][u - 1] = t

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] < INF and dist[k][j] < INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return min(max(i) for i in dist)


print(floyd_warshall())
