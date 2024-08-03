n = int(input())

ans = 0
for a in range(1, int(n ** (1 / 3)) + 1):
    for b in range(a, int((n // a) ** (1 / 2)) + 1):
        max_c = n // (a * b)
        ans += max_c - b + 1

print(ans)
