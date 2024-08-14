import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
in_degree = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    in_degree[b] += 1


def topological_sort():
    res = []
    heap = [i for i in range(N) if in_degree[i] == 0]
    heapq.heapify(heap)

    while heap:
        v = heapq.heappop(heap)
        res.append(v + 1)

        for nv in graph[v]:
            in_degree[nv] -= 1
            if in_degree[nv] == 0:
                heapq.heappush(heap, nv)

    return res if len(res) == N else -1


ans = topological_sort()
if ans == -1:
    print(-1)
else:
    print(*ans)
