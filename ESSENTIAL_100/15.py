from itertools import permutations
from math import factorial, dist

n = int(input())
xy = []
for _ in range(n):
    a, b = map(int, input().split())
    xy.append((a, b))

sum_dis = sum(
    dist(perm[i], perm[i + 1]) for i in range(n - 1) for perm in permutations(xy)
)

print(sum_dis / factorial(n))
