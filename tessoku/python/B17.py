n = int(input())
h = list(map(int, input().split()))

dp = [0] * n
dp[1] = abs(h[0] - h[1])
for i in range(2, n):
    one = dp[i - 1] + abs(h[i] - h[i - 1])
    two = dp[i - 2] + abs(h[i] - h[i - 2])
    dp[i] = min(one, two)

ans = []
curr = n - 1
while curr >= 0:
    ans.append(curr + 1)
    if curr == 0:
        break
    if dp[curr] == dp[curr - 1] + abs(h[curr] - h[curr - 1]):
        curr -= 1
    else:
        curr -= 2

print(len(ans))
print(" ".join(map(str, reversed(ans))))
