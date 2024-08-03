from collections import defaultdict
from typing import DefaultDict

n = int(input())
a = list(map(int, input().split()))
a = [e % 200 for e in a]

hashmap: DefaultDict[int, int] = defaultdict(int)
for e in a:
    hashmap[e] += 1

ans = 0
for v in hashmap.values():
    ans += v * (v - 1) // 2

print(ans)
