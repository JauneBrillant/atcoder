n, s = map(int, input().split())
a = list(map(int, input().split()))

ok = False
for bit in range(1 << n):
    total = 0
    for i in range(n):
        if bit & (1 << i):
            total += a[i]

    if total == s:
        ok = True

print("Yes" if ok else "No")
