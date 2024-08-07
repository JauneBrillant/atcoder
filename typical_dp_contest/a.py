n = int(input())
p = [0] + list(map(int, input().split()))
max_point = 100 * n + 1

# dp[i][j] := i問目までで合計得点をj点にできるか
dp = [[False] * max_point for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = True

for i in range(1, n + 1):
    for j in range(max_point):
        if j == p[i]:
            dp[i][j] = True
        if j >= p[i] and dp[i - 1][j - p[i]]:
            dp[i][j] = True
        else:
            dp[i][j] = dp[i - 1][j]

print(sum(1 for b in dp[n] if b))
