from itertools import combinations

n = int(input())
coordinates = []
for _ in range(n):
    coordinates.append(tuple(map(int, input().split())))
coordinates.sort()
st = set(coordinates)

ans = 0
for p1, p2 in combinations(coordinates, 2):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = (x2 + (y2 - y1), y2 - (x2 - x1))
    x4, y4 = (x1 + (y2 - y1), y1 - (x2 - x1))

    if (x3, y3) in st and (x4, y4) in st:
        edge_len = (y2 - y1) + (x2 - x1)
        ans = max(ans, (y2 - y1) ** 2 + (x2 - x1) ** 2)

print(ans)
