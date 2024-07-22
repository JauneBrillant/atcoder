n, m = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
curr = 0
for i in range(m):
    sum += a[i]
    curr += (i + 1) * a[i]

ans = curr
for i in range(m, n):
    ans = max(ans, curr - sum + a[i] * m)
    curr = curr - sum + a[i] * m
    sum = sum - a[i - m] + a[i]

print(ans)
