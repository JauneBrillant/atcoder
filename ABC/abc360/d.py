import bisect

n, t = map(int, input().split())
s = input()
x = list(map(int, input().split()))

pos_ants = []
neg_ants = []
for i in range(n):
    if s[i] == "1":
        pos_ants.append(x[i] + t)
    else:
        neg_ants.append(x[i] - t)

neg_ants.sort()

ans = 0
for pos in pos_ants:
    idx = bisect.bisect(x, pos - t)
    ans += len(neg_ants) - idx

print(ans)
