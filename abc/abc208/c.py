from collections import defaultdict
from typing import DefaultDict

n, k = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)

rest = k % n
hashmap: DefaultDict[int, int] = defaultdict(lambda: k // n)

for num in sorted_a:
    if rest <= 0:
        break
    hashmap[num] += 1
    rest -= 1

for num in a:
    print(hashmap[num])
