h, w, n = map(int, input().split())
x = [[0] * (w + 9) for _ in range(h + 9)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    x[a][b] += 1
    x[a][d + 1] -= 1
    x[c + 1][b] -= 1
    x[c + 1][d + 1] += 1

for i in range(1, h + 3):
    for j in range(1, w + 3):
        x[i][j] += x[i][j - 1]

for i in range(1, w + 3):
    for j in range(1, h + 3):
        x[j][i] += x[j - 1][i]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(x[i][j], end=" ")
    print()
