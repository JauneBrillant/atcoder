from bisect import bisect_right

n, m = map(int, input().split())
p = [0]
for _ in range(n):
    p.append(int(input()))

s = []
for p1 in p:
    for p2 in p:
        s.append(p1 + p2)
s.sort()

ans = 0
for curr_p in s:
    if m < curr_p:
        break
    pos = bisect_right(s, m - curr_p) - 1
    ans = max(ans, curr_p + s[pos])

print(ans)
