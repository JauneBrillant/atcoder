from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))

hashmap = defaultdict(list)
for i, e in enumerate(a):
    hashmap[e].append(i + 1)

for _ in range(q):
    x, y = map(int, input().split())
    if y - 1 < len(hashmap[x]):
        print(hashmap[x][y - 1])
    else:
        print(-1)
