N, M = map(int, input().split())
V = []
W = []
for _ in range(N):
    v, w = map(int, input().split())
    V.append(v)
    W.append(w)

# dp[N] := 重さNでの最大価値
dp = [0] * (M + 1)

for i in range(1, M + 1):
    for j in range(N):
        if i >= W[j]:
            dp[i] = max(dp[i], dp[i - W[j]] + V[j])

print(dp[M])
