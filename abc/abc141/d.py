from heapq import heapify, heappush, heappop

N, M = map(int, input().split())
A = list(map(lambda x: int(x) * -1, input().split()))

heapify(A)
for _ in range(M):
    x = heappop(A) * -1
    heappush(A, -(x // 2))

print(abs(sum(A)))
