from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

index_map = defaultdict(list)
for i, e in enumerate(a):
    index_map[e].append(i)

res = [0] * n
for i, (k, v) in enumerate(sorted(index_map.items()), 1):
    for idx in v:
        res[idx] = i

print("\n".join(map(str, res)))
