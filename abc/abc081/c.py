from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

hashmap = defaultdict(int)
for e in a:
    hashmap[e] += 1

sorted_values = list(sorted(hashmap.values()))
types = len(sorted_values)

ans = 0
for i in range(types - k):
    ans += sorted_values[i]

print(ans)
