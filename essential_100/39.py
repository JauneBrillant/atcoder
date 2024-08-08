# from tabulate import tabulate

N = int(input())
A = list(map(int, input().split()))
numbers = A[: N - 1]
res = A[-1]

# dp[i][j] := i番目までの数字を使って、数字jの作り方の通り
dp = [[0] * 21 for _ in range(len(numbers))]
dp[0][A[0]] = 1

for i in range(1, len(numbers)):
    for j in range(21):
        if j + numbers[i] < 21:
            dp[i][j + numbers[i]] += dp[i - 1][j]
        if j - numbers[i] >= 0:
            dp[i][j - numbers[i]] += dp[i - 1][j]

print(dp[len(numbers) - 1][res])
# print(tabulate(dp, tablefmt="grid"))
