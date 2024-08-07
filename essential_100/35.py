N, M = map(int, input().split())
V = [0]
W = [0]
for _ in range(N):
    v, w = map(int, input().split())
    V.append(v)
    W.append(w)

# dp[i][j] := 品物iまで選んだ時の重さ制限jまででの最大価値
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(M + 1):
        if j < W[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i])

print(dp[N][M])
