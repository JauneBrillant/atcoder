MOD = 10**9 + 7
n, m = map(int, input().split())
ng = [False] * (n + 1)
for _ in range(m):
    x = int(input())
    ng[x] = True

# 貰うDP
# dp = [0] * (n + 1)
# dp[0] = 1
# for i in range(1, n + 1):
#     if ng[i]:
#         continue
#     dp[i] += dp[i - 1]
#     if i > 1:
#         dp[i] += dp[i - 2]
#     dp[i] %= MOD

# print(dp[n])


# 配るDP
dp = [0] * (n + 1)
dp[0] = 1
for i in range(n):
    if not ng[i + 1]:
        dp[i + 1] += dp[i]
    if i + 2 < n + 1 and not ng[i + 2]:
        dp[i + 2] += dp[i]

print(dp[n] % MOD)
