from heapq import heapify, heappush, heappop

N, M = map(int, input().split())
G = [[] for _ in range(N)]
in_degree = [0] * N
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    in_degree[v] += 1


def topological_sort():
    res = []
    heap = [i for i in range(N) if in_degree[i] == 0]
    heapify(heap)

    while heap:
        u = heappop(heap)
        res.append(u + 1)

        for v in G[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heappush(heap, v)

    return res if len(res) == N else -1


res = topological_sort()
if res == -1:
    print(-1)
else:
    print(*res)
