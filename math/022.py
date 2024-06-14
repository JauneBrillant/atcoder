from collections import defaultdict
from typing import Dict

n = int(input())
a = list(map(int, input().split()))

map: Dict[int, int] = defaultdict(int)
ans = 0

for e in a:
    complement = 100000 - e
    if complement in map:
        ans += map[complement]

    map[e] += 1

print(ans)
