n, w = map(int, input().split())
values = [0]
weights = [0]
for _ in range(n):
    a, b = map(int, input().split())
    values.append(a)
    weights.append(b)

# dp[i][j]
# i番目までの商品から重さの総和がj以下になるように選んだ時の、価値の和の最大値

dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(w + 1):
        if j < weights[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])

print(dp[n][w])
