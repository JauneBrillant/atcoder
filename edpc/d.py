n, w = map(int, input().split())
weight = [0]
value = [0]
for _ in range(n):
    we, val = map(int, input().split())
    weight.append(we)
    value.append(val)

# dp[i][j] := iまでの商品で制限重量jの時の最大価値
dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(w + 1):
        if j < weight[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

print(dp[n][w])
