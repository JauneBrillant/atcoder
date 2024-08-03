from itertools import combinations

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for t1, t2 in combinations([i for i in range(m)], 2):
    points = 0
    for student in range(n):
        p = max(a[student][t1], a[student][t2])
        points += p
    ans = max(ans, points)

print(ans)
