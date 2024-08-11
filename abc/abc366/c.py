from collections import defaultdict

Q = int(input())
hashmap = defaultdict(int)

for _ in range(Q):
    query = list(map(int, input().split()))
    t = query[0]
    t = map(int, input().split())

    if t == 1:
        x = query[1]
        hashmap[x] += 1
    if t == 2:
        # x = query[1]
        hashmap[x] -= 1
        if hashmap[x] == 0:
            hashmap.pop(x)
    if t == 3:
        print(len(hashmap))
