from heapq import heappush, heappop

Q = int(input())
heap = []
add = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    type = query[0]

    match type:
        case 1:
            x = query[1]
            heappush(heap, x - add)
        case 2:
            x = query[1]
            add += x
        case 3:
            print(heappop(heap) + add)
