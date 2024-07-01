n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort()

deposit = k
pos = 0
prev = 0
for a, b in ab:
    if deposit - (a - pos) < 0:
        break
    if prev != a:
        deposit -= a - pos
    pos = a
    deposit += b
    prev = a

print(pos + deposit)
