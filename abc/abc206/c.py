from collections import defaultdict
from typing import DefaultDict

n = int(input())
a = list(map(int, input().split()))

hashmap: DefaultDict[int, int] = defaultdict(int)

ans = 0
for i in range(n):
    ans += i - hashmap[a[i]]
    hashmap[a[i]] += 1

print(ans)
