n = int(input())
s = "x" + input()

# dp[i][j] := jラウンド目でiの手を出した時の最大勝利数
dp = [[0] * (n + 1) for _ in range(3)]

# 0 : R
# 1 : P
# 2 : S

for j in range(1, n + 1):
    for i in range(3):
        if s[j] == "R":
            if i == 0:
                dp[i][j] = max(dp[1][j - 1], dp[2][j - 1])
            if i == 1:
                dp[i][j] = max(dp[0][j - 1], dp[2][j - 1]) + 1
        if s[j] == "P":
            if i == 1:
                dp[i][j] = max(dp[0][j - 1], dp[2][j - 1])
            if i == 2:
                dp[i][j] = max(dp[0][j - 1], dp[1][j - 1]) + 1
        if s[j] == "S":
            if i == 2:
                dp[i][j] = max(dp[0][j - 1], dp[1][j - 1])
            if i == 0:
                dp[i][j] = max(dp[1][j - 1], dp[2][j - 1]) + 1

print(max(dp[0][n], dp[1][n], dp[2][n]))
