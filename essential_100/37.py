N, M = map(int, input().split())
C = list(map(int, input().split()))
mn = min(C)

# dp[n] := n円を支払う時のコインの最小枚数
dp = [float("inf")] * (N + 1)
dp[0] = 0
for n in range(mn, N + 1):
    for c_amount in C: 
        if c_amount <= n:
            dp[n] = min(dp[n], dp[n - c_amount] + 1)

print(dp[N])

