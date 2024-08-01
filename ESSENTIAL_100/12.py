from itertools import combinations

n, m = map(int, input().split())
xy = []
for _ in range(m):
    x, y = map(int, input().split())
    xy.append((x, y))
xy_st = set(xy)

ans = 0
for bit in range(1 << n):
    people = []
    for i in reversed(range(n)):
        if bit >> i & 1:
            people.append(i + 1)

    for x, y in combinations(people, 2):
        if (x, y) not in xy_st and (y, x) not in xy_st:
            break
    else:
        ans = max(ans, len(people))

print(ans)
