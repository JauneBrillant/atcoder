N, M = map(int, input().split())
G = [[0] * (N + 9) for _ in range(N + 9)]

for _ in range(M):
    a, b, x = map(int, input().split())
    G[a][b] += 1
    G[a][b + 1] -= 1

    G[a + x + 1][b] -= 1
    G[a + x + 1][b + x + 2] += 1

    G[a + x + 2][b + 1] += 1
    G[a + x + 2][b + x + 2] -= 1

for i in range(1, N + 2):
    for j in range(1, N + 2):
        G[i][j] += G[i][j - 1]

for i in range(1, N + 2):
    for j in range(1, N + 2):
        G[j][i] += G[j - 1][i]

for i in range(1, N + 2):
    for j in range(1, N + 2):
        G[i][j] += G[i - 1][j - 1]

print(sum(1 for i in range(N + 2) for j in range(N + 2) if G[i][j] > 0))
