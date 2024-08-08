from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N):
    v, cnt, *nv = map(int, input().split())
    G[v - 1] = [x - 1 for x in nv]

deq = deque([(0, 0)])
dist = [-1] * N
dist[0] = 0

while deq:
    v, depth = deq.popleft()

    for nv in G[v]:
        if dist[nv] == -1:
            dist[nv] = depth + 1
            deq.append((nv, depth + 1))

for i in range(N):
    print(i + 1, dist[i])
