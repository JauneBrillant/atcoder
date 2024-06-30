from bisect import bisect

n, t = map(int, input().split())
s = input()
x = list(map(int, input().split()))

neg_ants = []
for i in range(n):
    if s[i] == "0":
        neg_ants.append(x[i])
neg_ants.sort()

ans = 0
for i in range(n):
    if s[i] == "1":
        ans += bisect(neg_ants, x[i] + 2 * t) - bisect(neg_ants, x[i])

print(ans)
