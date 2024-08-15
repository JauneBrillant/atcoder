N, M = map(int, input().split())
edges = list(tuple(map(int, input().split())) for _ in range(M))


def floyd_warshall():
    INF = float("inf")
    dist = [[0 if i == j else INF for j in range(N)] for i in range(N)]

    for s, t, d in edges:
        dist[s][t] = min(dist[s][t], d)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] < INF and dist[k][j] < INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for i in range(N):
        if dist[i][i] < 0:
            return "NEGATIVE CYCLE"

    return "\n".join(
        " ".join("INF" if dist[i][j] == INF else str(dist[i][j]) for j in range(N))
        for i in range(N)
    )


res = floyd_warshall()
print(res)
