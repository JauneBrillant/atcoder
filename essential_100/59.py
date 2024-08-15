# N個の街、K本の道路(無指向)
# 街１から街Kまで行く
# 街それぞれにタクシー会社があり、利用した距離に関わらずCi円、Ri本の道路しか通れない
# 街Nに到着するための運賃の最小値を求めろ

from heapq import heappush, heappop
from collections import deque

N, K = map(int, input().split())
C = []
R = []
for _ in range(N):
    c, r = map(int, input().split())
    C.append(c)
    R.append(r)
G = [[] for _ in range(N)]
for _ in range(K):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)


def dijkstra(start, end):
    heap = [(0, start)]
    costs = [float("inf")] * N
    costs[start] = 0

    while heap:
        curr_cost, v = heappop(heap)
        if curr_cost > costs[v]:
            continue
        for nv in graph[v]:
            new_cost = curr_cost + C[v]
            if new_cost < costs[nv]:
                costs[nv] = new_cost
                heappush(heap, (new_cost, nv))

    return costs[end]


def bfs(start, limit):
    dists = [-1] * N
    dists[start] = 0
    q = deque([start])

    while q:
        v = q.popleft()
        for nv in G[v]:
            if dists[nv] == -1:
                dists[nv] = dists[v] + 1
                q.append(nv)

    return set([i for i in range(N) if dists[i] <= limit and i != start])


graph = [set() for _ in range(N)]
for i in range(N):
    graph[i] |= bfs(i, R[i])

print(dijkstra(0, N - 1))
