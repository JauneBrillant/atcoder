from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

hashmap = defaultdict(int)
for e in a:
    hashmap[e] += 1

ans = 0
for v in hashmap.values():
    ans += v // 2

print(ans)
