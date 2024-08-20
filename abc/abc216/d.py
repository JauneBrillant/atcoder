from collections import defaultdict
from collections import deque

N, M = map(int, input().split())
K = []
A = []
for _ in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    K.append(k)
    A.append(a)

top = defaultdict(list)
for i, a in enumerate(A):
    top[a[0]].append((i, 0))

que = deque([(k, v) for k, v in top.items() if len(top[k]) == 2])

while que:
    key, values = que.popleft()
    a, a_dep, b, b_dep = *values[0], *values[1]
    top.pop(key)

    if a_dep + 1 < K[a]:
        val = A[a][a_dep + 1]
        top[val].append((a, a_dep + 1))
        if len(top[val]) == 2:
            que.append((val, top[val]))

    if b_dep + 1 < K[b]:
        num = A[b][b_dep + 1]
        top[num].append((b, b_dep + 1))
        if len(top[num]) == 2:
            que.append((num, top[num]))


print("Yes" if not top else "No")
