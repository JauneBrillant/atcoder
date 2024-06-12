n = int(input())
x = [[0] * 1509 for _ in range(1509)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    x[a][b] += 1
    x[a][d] -= 1
    x[c][b] -= 1
    x[c][d] += 1

for i in range(1501):
    for j in range(1, 1501):
        x[i][j] += x[i][j - 1]

for i in range(1501):
    for j in range(1, 1501):
        x[j][i] += x[j - 1][i]

ans = sum(1 for i in range(1501) for j in range(1501) if x[i][j] > 0)
print(ans)
