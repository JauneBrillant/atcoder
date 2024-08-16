H, W = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(10)]
B = [list(map(int, input().split())) for _ in range(H)]


def floyd_warshall():
    for k in range(10):
        for i in range(10):
            for j in range(10):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])


floyd_warshall()

ans = 0
for i in range(H):
    for j in range(W):
        if B[i][j] == -1:
            continue
        ans += G[B[i][j]][1]

print(ans)
