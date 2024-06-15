n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)

i = 0
j = 0
ans = 0
while i < n and j < m:
    if a[i] >= b[j]:
        ans += a[i]
        i += 1
        j += 1
    else:
        i += 1

if j == m:
    print(ans)
else:
    print(-1)
