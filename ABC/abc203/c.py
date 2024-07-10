n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort()

for a, b in ab:
    if a <= k:
        k += b

print(k)
