n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

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

print(ans if j == m else -1)
