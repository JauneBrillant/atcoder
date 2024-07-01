from collections import defaultdict
from typing import DefaultDict

n = int(input())
a = list(map(int, input().split()))

counts: DefaultDict[int, int] = defaultdict(int)
for e in a:
    counts[e % 200] += 1

ans = 0
for v in counts.values():
    ans += v * (v - 1)

print(ans // 2)
