n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 10**9
for i in range(k + 1):
    ans = min(a[i + n - k - 1] - a[i], ans)

print(ans)
