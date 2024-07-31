n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(s + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
        if j >= a[i - 1] and dp[i - 1][j - a[i - 1]]:
            dp[i][j] = True

# N番目のカードを選ぶかどうかの判定が理解できていない
if dp[n][s]:
    ans = []
    place = s
    for i in range(n, 0, -1):
        if dp[i - 1][place]:
            place -= 0
        else:
            place -= a[i - 1]
            ans.append(i)
    ans.reverse()
    print(len(ans))
    print(" ".join(map(str, ans)))
else:
    print(-1)
