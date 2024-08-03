from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(a + b)
hashmap = defaultdict(int)
for i, c in enumerate(c):
    hashmap[c] = i + 1

print(" ".join(str(hashmap[e]) for e in a))
print(" ".join(str(hashmap[e]) for e in b))
