n = int(input())
a = [0]
b = [0]
c = [0]
for _ in range(n):
    x, y, z = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)

# dp[i][j] := i日目でjを遊んだ時の幸福度の最大値
dp = [[0] * (n + 1) for _ in range(3)]

for i in range(1, n + 1):
    for j in range(3):
        if j == 0:
            dp[j][i] = max(dp[1][i - 1], dp[2][i - 1]) + a[i]
        if j == 1:
            dp[j][i] = max(dp[0][i - 1], dp[2][i - 1]) + b[i]
        if j == 2:
            dp[j][i] = max(dp[0][i - 1], dp[1][i - 1]) + c[i]

print(max(dp[0][n], dp[1][n], dp[2][n]))
