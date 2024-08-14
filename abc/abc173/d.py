import heapq

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

heap = [A[0] * -1]
ans = 0

for i in range(1, N):
    ans += abs(heapq.heappop(heap))
    heapq.heappush(heap, A[i] * -1)
    heapq.heappush(heap, A[i] * -1)

print(ans)
