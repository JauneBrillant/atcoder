n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[False] * n for _ in range(2)]
dp[0][0] = True
dp[1][0] = True

for i in range(1, n):
    if dp[0][i - 1]:
        if abs(a[i - 1] - a[i]) <= k:
            dp[0][i] = True
        if abs(a[i - 1] - b[i]) <= k:
            dp[1][i] = True
    if dp[1][i - 1]:
        if abs(b[i - 1] - a[i]) <= k:
            dp[0][i] = True
        if abs(b[i - 1] - b[i]) <= k:
            dp[1][i] = True

print("Yes" if dp[0][n - 1] or dp[1][n - 1] else "No")
