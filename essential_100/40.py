MOD = 10000
N, K = map(int, input().split())
sche = {}
for _ in range(K):
    a, b = map(int, input().split())
    sche[a] = b - 1


# 晩御飯を食べる場合の数がどれだけあるか
# ただし、三日以上同じものを食べてはいけない

# dp[i][j][0] := 前日にjではないパスタを食べた時の、i日目にjを食べる場合の数
# dp[i][j][1] := 前日にjを食べた時の、i日目にjを食べる場合の数

dp = [[[0, 0] for _ in range(3)] for _ in range(N + 1)]
if 1 in sche:
    dp[1][sche[1]][0] = 1
else:
    for j in range(3):
        dp[1][j][0] = 1

for i in range(2, N + 1):
    # スケジュールが決まっている場合
    if i in sche:
        for k in range(3):
            if sche[i] != k:
                dp[i][sche[i]][0] += (dp[i - 1][k][0] + dp[i - 1][k][1]) % MOD
        dp[i][sche[i]][1] += dp[i - 1][sche[i]][0]

    else:
        for j in range(3):
            for k in range(3):
                if k != j:  # 前日とは違うものを食べる時の場合の数
                    dp[i][j][0] += (dp[i - 1][k][0] + dp[i - 1][k][1]) % MOD
            dp[i][j][1] += dp[i - 1][j][0]


# print(tabulate(dp, headers=["A", "B", "C"]))
ans = sum(sum(dp[N][j]) for j in range(3)) % MOD
print(ans % MOD)
