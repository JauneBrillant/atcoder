while True:
    n = int(input())
    if n == 0:
        exit()

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n + 1):
        if i + 1 <= n:
            dp[i + 1] += dp[i]
        if i + 2 <= n:
            dp[i + 2] += dp[i]
        if i + 3 <= n:
            dp[i + 3] += dp[i]
    print((((dp[n] + 9) // 10) + 364) // 365)
