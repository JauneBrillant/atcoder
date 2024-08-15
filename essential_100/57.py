# 頂点がN個でa, b間の辺の重みの総和の最小を求める
# グラフの辺の情報は最初はなく、その都度追加される

from heapq import heappush, heappop


def dijkstra(start, end):
    heap = [(0, start)]
    fees = [float("inf")] * N
    fees[start] = 0

    while heap:
        curr_fee, v = heappop(heap)
        if curr_fee > fees[v]:
            continue

        for nv, w in G[v]:
            new_fee = curr_fee + w
            if new_fee < fees[nv]:
                fees[nv] = new_fee
                heappush(heap, (new_fee, nv))

    return fees[end]


N, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(K):
    query = list(map(int, input().split()))
    type = query[0]

    match type:
        case 0:
            start, end = query[1:3]
            res = dijkstra(start - 1, end - 1)
            if res == float("inf"):
                print(-1)
            else:
                print(res)

        case 1:
            u, v, w = query[1:4]
            u -= 1
            v -= 1
            G[u].append((v, w))
            G[v].append((u, w))
