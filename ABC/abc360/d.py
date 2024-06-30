import bisect

n, t = map(int, input().split())
s = input()
x = list(map(int, input().split()))

pos_ants = []
neg_ants = []
for i in range(n):
    if s[i] == "1":
        pos_ants.append(x[i])
    else:
        neg_ants.append(x[i])

pos_ants.sort()
neg_ants.sort()

ans = 0
for p in pos_ants:
    r = p + t * 2
    ans += bisect.bisect(neg_ants, r) - bisect.bisect(neg_ants, p)

print(ans)
