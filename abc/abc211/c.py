MOD = 10 ** 9 + 7
S = input()
T = "chokudai"
N = len(S)
M = len(T)

# dp[i][j] := Sのj文字目までを"chokudai"のi文字目までで何通り作れるか
dp = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(N + 1):
    dp[0][i] = 1

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if T[i - 1] == S[j - 1]:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD
        else:
            dp[i][j] = dp[i][j - 1]

print(dp[M][N])
        
