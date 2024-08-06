n = int(input())

dp = [float("inf")] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = 1 + dp[i - 1]

    power = 6
    while power <= i:
        dp[i] = min(dp[i], 1 + dp[i - power])
        power *= 6

    power = 9
    while power <= i:
        dp[i] = min(dp[i], 1 + dp[i - power])
        power *= 9

print(dp[n])
