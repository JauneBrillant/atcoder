H, W, K, V = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
acc = [[0] * (W + 2) for _ in range(H + 2)]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        acc[i][j] = A[i - 1][j - 1]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        acc[i][j] += acc[i][j - 1]

for i in range(1, W + 1):
    for j in range(1, H + 1):
        acc[j][i] += acc[j - 1][i]

ans = 0
for a in range(1, H + 1):
    for b in range(1, W + 1):
        for c in range(a, H + 1):
            for d in range(b, W + 1):
                v = acc[c][d] + acc[a - 1][b - 1] - acc[c][b - 1] - acc[a - 1][d]
                cnt = (c * d) + (a - 1) * (b - 1) - (c * (b - 1)) - ((a - 1) * d)
                # print(v, cnt)
                if v + K * cnt <= V:
                    ans = max(ans, cnt)
print(ans)
