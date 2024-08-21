N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

# dp[i][j] := i番目まで操作に関わった時、先頭がjになる場合の数
dp = [[0] * 10 for _ in range(N)]
a, b = A[0], A[1]
dp[1][(a + b) % 10] += 1
dp[1][a * b % 10] += 1

for i in range(1, N - 1):
    for j in range(10):
        dp[i + 1][(j + A[i + 1]) % 10] += dp[i][j]
        dp[i + 1][(j * A[i + 1]) % 10] += dp[i][j]
        dp[i + 1][(j + A[i + 1]) % 10] %= MOD
        dp[i + 1][(j * A[i + 1]) % 10] %= MOD

print(*dp[N - 1])
