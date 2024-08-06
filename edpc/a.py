n = int(input())
h = list(map(int, input().split()))

# 貰うDP

# dp = [0] * n
# dp[1] = abs(h[0] - h[1])
# for i in range(2, n):
#     one_step = dp[i - 1] + abs(h[i - 1] - h[i])
#     two_step = dp[i - 2] + abs(h[i - 2] - h[i])
#     dp[i] = min(one_step, two_step)

# print(dp[n - 1])


# 配るDP

dp = [float("inf")] * n
dp[0] = 0
for i in range(n - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
    if i + 2 < n:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))

print(dp[n - 1])
