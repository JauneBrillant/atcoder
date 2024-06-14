from itertools import combinations

n, k = map(int, input().split())
a = list(map(int, input().split()))

ok = False
front = a[: n // 2]
back = a[n // 2 :]

subsets_front = set(
    sum(subset) for i in range(len(front) + 1) for subset in combinations(front, i)
)
subsets_back = set(
    sum(subset) for i in range(len(back) + 1) for subset in combinations(back, i)
)

for x in subsets_front:
    if k - x in subsets_back:
        ok = True

print("Yes" if ok else "No")
