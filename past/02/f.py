from collections import defaultdict
from heapq import heappush, heappop

N = int(input())
AB = list(tuple(map(int, input().split())) for _ in range(N))

tasks = defaultdict(list)
for a, b in AB:
    tasks[a].append(b)

heap = []
total = 0
for day in range(1, N + 1):
    for val in tasks[day]:
        heappush(heap, -val)

    if len(heap) > 0:
        total += abs(heappop(heap))
    print(total)
