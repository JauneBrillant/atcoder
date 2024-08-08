X = int(input())

# 1
# ABCDEF
# ABBCCD

# dp[i][j] := sのi文字目までと、tのj文字目までの最長共通部分列
# s[i] == t[j] これらが一致したということは新しい部分文字列が作れるということ
# 新しくできる最長部分文字列の長さ = 前の最長部分文字列の長さ+1ということ


def solve(s, t, n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


for _ in range(X):
    S = input()
    T = input()
    print(solve(S, T, len(S), len(T)))
