from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
in_degree = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1


def topological_sort():
    res = []
    deq = deque([i for i in range(N) if in_degree[i] == 0])

    while deq:
        v = deq.popleft()
        res.append(v)

        for nv in graph[v]:
            in_degree[nv] -= 1
            if in_degree[nv] == 0:
                deq.append(nv)

    return res


res = topological_sort()
for v in res:
    print(v)
