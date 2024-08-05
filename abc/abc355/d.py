from bisect import bisect_right

n = int(input())
lr = []
l = []
for _ in range(n):
    left, right = map(int, input().split())
    lr.append((left, right))
    l.append(left)
lr.sort()
l.sort()

ans = 0
for i, (_, r) in enumerate(lr):
    ans += bisect_right(l, r) - i - 1

print(ans)
