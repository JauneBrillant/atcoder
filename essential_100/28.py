from collections import deque

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n):
    line = list(map(int, input().split()))
    u = line[0] - 1
    m = line[1]
    for i in range(m):
        v = line[2 + i] - 1
        g[u].append(v)

node_depth = [-1] * n
node_depth[0] = 0
d = deque([0])

while d:
    v = d.popleft()
    current_depth = node_depth[v]

    for nv in g[v]:
        if node_depth[nv] == -1:
            node_depth[nv] = current_depth + 1
            d.append(nv)

for i, depth in enumerate(node_depth):
    print(i + 1, depth)
