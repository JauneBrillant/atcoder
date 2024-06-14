# import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))

# ans = 0
# for i, e in enumerate(a):
#     ans += bisect.bisect(a, e + k) - i - 1

# print(ans)

ans = 0
r = 0
for l in range(n):
    while r < n and a[r] - a[l] <= k:
        r += 1
    ans += r - l - 1

print(ans)
