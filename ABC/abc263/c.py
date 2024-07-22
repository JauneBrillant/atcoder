from itertools import combinations

n, m = map(int, input().split())
ans = combinations(range(1, m + 1), n)
for pair in ans:
    print(" ".join(map(str, pair)))
