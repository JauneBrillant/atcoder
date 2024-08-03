from bisect import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

ans = 10**9
for num in a:
    idx = bisect(b, num)

    if idx < m:
        ans = min(ans, abs(num - b[idx]))
    if idx > 0:
        ans = min(ans, abs(num - b[idx - 1]))

print(ans)
