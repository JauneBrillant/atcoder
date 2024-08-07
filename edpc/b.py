n, k = map(int, input().split())
h = list(map(int, input().split()))

# dp[i] := 位置i までのコストの最小値

# 貰うDP
# dp = [float("inf")] * n
# dp[0] = 0

# for i in range(1, n):
#     for j in range(1, k + 1):
#         if i - j < 0:
#             break
#         dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))

# print(dp[n - 1])


# 配るDP
dp = [float("inf")] * n
dp[0] = 0
for i in range(n - 1):
    for j in range(1, k + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))

print(dp[n - 1])
