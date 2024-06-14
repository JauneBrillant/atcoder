n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] * 2 + list(map(int, input().split()))

dp = [0] * n
dp[1] = a[1]
for i in range(2, n):
    one = dp[i - 1] + a[i]
    two = dp[i - 2] + b[i]
    dp[i] = min(one, two)

ans = []
curr = n - 1
while curr >= 0:
    ans.append(curr + 1)
    if dp[curr] == dp[curr - 1] + a[curr]:
        curr -= 1
    else:
        curr -= 2

print(len(ans))
print(" ".join(map(str, reversed(ans))))
