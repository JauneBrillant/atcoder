from collections import defaultdict
from typing import DefaultDict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt_a: DefaultDict[int, int] = defaultdict(int)
for ai in a:
    cnt_a[ai] += 1


ans = 0
for ci in c:
    ans += cnt_a[b[ci - 1]]
print(ans)
