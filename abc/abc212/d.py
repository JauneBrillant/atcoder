import heapq

Q = int(input())

heap = []
res = []
add = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    type = query[0]

    match type:
        case 1:
            x = query[1]
            heapq.heappush(heap, x - add)
        case 2:
            x = query[1]
            add += x
        case 3:
            res.append(heapq.heappop(heap) + add)

print(*res)
