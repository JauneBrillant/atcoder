import sys
import heapq

N, M, S = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    s, t, d = map(int, input().split())
    G[s].append((t, d))


def dijkstra(graph, start):
    distance = [sys.maxsize] * N
    distance[start] = 0
    heap = [(start, 0)]

    while heap:
        u, dist = heapq.heappop(heap)
        if dist > distance[u]:
            continue
        for v, weight in graph[u]:
            new_distance = dist + weight
            if new_distance < distance[v]:
                distance[v] = new_distance
                heapq.heappush(heap, (v, new_distance))

    return distance


lst = dijkstra(G, S)
for dst in lst:
    if dst == sys.maxsize:
        print("INF")
    else:
        print(dst)
