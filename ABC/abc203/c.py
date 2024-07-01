n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort()
curr = k
for a, b in ab:
    if curr >= a:
        curr += b
    else:
        break

print(curr)
