n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] * 2 + list(map(int, input().split()))

dp = [0] * n
dp[1] = a[1]
for i in range(2, n):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i])

print(dp[n - 1])
