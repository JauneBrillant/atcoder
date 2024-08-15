import heapq

N, M, R = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, d = map(int, input().split())
    G[u].append((v, d))


def dijkstra2(graph, start):
    heap = [(0, start)]
    dist = [float("inf")] * N
    dist[start] = 0

    while heap:
        curr_dist, v = heapq.heappop(heap)

        # if curr_dist > dist[v]:
        #     continue
        for nv, w in graph[v]:
            new_dist = curr_dist + w
            if new_dist < dist[nv]:
                dist[nv] = new_dist
                heapq.heappush(heap, (new_dist, nv))
    return dist


ans = dijkstra2(G, R)
for elem in ans:
    print(elem if elem != float("inf") else "INF")
