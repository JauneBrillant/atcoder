import sys

sys.setrecursionlimit(100000)

n, x = map(int, input().split())
ab = []
for _ in range(n):
    ai, bi = map(int, input().split())
    ab.append((ai, bi))

dp = [[False] * (x + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(x + 1):
        a, b = ab[i - 1]
        if dp[i - 1][j]:
            if j + a <= x:
                dp[i][j + a] = True
            if j + b <= x:
                dp[i][j + b] = True

print("Yes" if dp[n][x] else "No")
