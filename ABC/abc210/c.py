from collections import defaultdict
from typing import DefaultDict

n, k = map(int, input().split())
c = list(map(int, input().split()))

hashmap: DefaultDict[int, int] = defaultdict(int)
st = set()
ans = 0

for i in range(n):
    hashmap[c[i]] += 1
    st.add(c[i])
    if i >= k - 1:
        ans = max(ans, len(st))
        idx = i - k + 1
        hashmap[c[idx]] -= 1
        if hashmap[c[idx]] == 0:
            st.remove(c[idx])

print(ans)
