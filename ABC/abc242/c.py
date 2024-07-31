import sys

sys.setrecursionlimit(1000000)
MOD = 998244353

n = int(input())
dp = [[0] * (n) for _ in range(10)]
for i in range(10):
    dp[i][0] = 1

print(dp)
