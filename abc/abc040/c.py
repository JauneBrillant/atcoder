n = int(input())
a = list(map(int, input().split()))

# 配るDP
dp = [float("inf")] * n
dp[0] = 0

for i in range(n - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(a[i] - a[i + 1]))
    if i + 2 < n:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(a[i] - a[i + 2]))

print(dp[n - 1])

# 貰うDP
dp = [0] * n
dp[1] = abs(a[0] - a[1])

for i in range(2, n):
    one_step = dp[i - 1] + abs(a[i] - a[i - 1])
    two_step = dp[i - 2] + abs(a[i] - a[i - 2])
    dp[i] = min(one_step, two_step)

print(dp[n - 1])
