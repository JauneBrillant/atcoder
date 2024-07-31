from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
res = 0
for i, e in enumerate(a):
    res = max(res, bisect_left(a, e + m) - i)

print(res)
