from bisect import bisect

n, k = map(int, input().split())
points = []
for i in range(n):
    total = sum(list(map(int, input().split())))
    points.append(total)
sorted_points = sorted(points)

for p in points:
    if bisect(sorted_points, p + 300) >= n - k:
        print("Yes")
    else:
        print("No")
