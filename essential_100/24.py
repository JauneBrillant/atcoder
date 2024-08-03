n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    line = list(map(int, input().split()))
    u = line[0]
    k = line[1]
    for j in range(k):
        graph[u - 1].append(line[j + 2] - 1)


cnt = 0
d = [0] * n
f = [0] * n
visited = [False] * n


def dfs(v):
    global cnt
    cnt += 1
    d[v] = cnt
    visited[v] = True
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(neighbor)
    cnt += 1
    f[v] = cnt


for i in range(n):
    if not visited[i]:
        dfs(i)

for i in range(n):
    print(i + 1, d[i], f[i])
