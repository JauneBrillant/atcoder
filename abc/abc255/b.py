# xy座標にn個の点
# うちk個の点を中心に半径rで円を描く
# 全ての点が円に収まるような最小のrを求める

from math import sqrt
import sys

N, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
xy = list(tuple(map(int, input().split())) for _ in range(N))

ans = 0
for i in range(N):
    if i in A:
        continue
    min_dist = sys.maxsize
    for j in A:
        if i == j:
            continue
        x1, y1, x2, y2 = *xy[i], *xy[j]
        min_dist = min(min_dist, (x1 - x2) ** 2 + (y1 - y2) ** 2)
    ans = max(ans, min_dist)

print(ans**0.5)
