# N個の街、M本の道路(無指向)がある
# K個の街はいけない、またいけない町からS本以下の道路を通って行ける街を危険な街とする
# 街の移動後はコストが必要、危険な街 >> Q、安全な街 >> P
# 町1から町Nに行く。最小のコストを求めろ

from collections import deque
from heapq import heappush, heappop

N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
Z = set([int(input()) - 1 for _ in range(K)])
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)


def bfs(start):
    deq = deque([start])
    dist = [-1] * N
    dist[start] = 0

    while deq:
        v = deq.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                deq.append(nv)

    return set([i for i in range(N) if dist[i] <= S and i not in Z])


def dijkstra(start, end):
    heap = [(0, start)]
    fees = [float("inf")] * N
    fees[start] = 0

    while heap:
        curr_fee, v = heappop(heap)

        if curr_fee > fees[v]:
            continue

        for nv in G[v]:
            if nv in Z:
                continue
            new_fee = curr_fee
            if nv in danger_city and nv != N - 1:
                new_fee += Q
            if nv not in danger_city and nv != N - 1:
                new_fee += P
            if new_fee < fees[nv]:
                fees[nv] = new_fee
                heappush(heap, (new_fee, nv))
    return fees[N - 1]


# 危険な街リストを求める
danger_city = set()
for city in Z:
    danger_city |= bfs(city)

# 最短経路(最小費用）を求める
ans = dijkstra(0, N - 1)
print(ans)
