from collections import defaultdict
from typing import List, Dict
import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())

hashmap: Dict[int, List] = defaultdict(list)
for i, num in enumerate(a):
    hashmap[num].append(i + 1)

for _ in range(q):
    l, r, x = map(int, input().split())
    ans = bisect.bisect_right(hashmap[x], r) - bisect.bisect_left(hashmap[x], l)
    print(ans)
