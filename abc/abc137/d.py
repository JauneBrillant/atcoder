from collections import defaultdict
import heapq

N, M = map(int, input().split())
AB = list(tuple(map(int, input().split())) for _ in range(N))

jobs = defaultdict(list)
for a, b in AB:
    jobs[a].append(b)

heap = []
total = 0

for day in range(1, M + 1):
    for val in jobs[day]:
        heapq.heappush(heap, -val)

    if len(heap) > 0:
        total += abs(heapq.heappop(heap))

print(total)
