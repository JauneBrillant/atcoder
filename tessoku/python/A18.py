n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(1, n + 1):
    sum = 0
    for j in range(s + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
        if j >= a[i - 1] and dp[i - 1][j - a[i - 1]]:
            dp[i][j] = True


print("Yes" if dp[n][s] else "No")
