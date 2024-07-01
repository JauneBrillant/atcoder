from collections import defaultdict
from typing import DefaultDict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

counts: DefaultDict[int, int] = defaultdict(int)
for ci in c:
    counts[b[ci - 1]] += 1

ans = 0
for ai in a:
    ans += counts[ai]

print(ans)
