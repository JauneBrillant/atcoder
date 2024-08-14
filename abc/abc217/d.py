from collections import deque
import heapq

Q = int(input())

deq = deque()
heap = []

for _ in range(Q):
    query = list(map(int, input().split()))
    type = query[0]
    match type:
        case 1:
            x = query[1]
            deq.append(x)
        case 2:
            if len(heap) > 0:
                print(heapq.heappop(heap))
            else:
                print(deq.popleft())
        case 3:
            while deq:
                heapq.heappush(heap, deq.pop())
