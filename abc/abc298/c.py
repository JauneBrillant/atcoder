from collections import defaultdict
from sortedcontainers import SortedList, SortedSet

n = int(input())
q = int(input())

box = defaultdict(SortedList)
card = defaultdict(SortedSet)
for _ in range(q):
    query = list(map(int, input().split()))
    type = query[0]

    if type == 1:
        i, j = query[1], query[2]
        box[j].add(i)
        card[i].add(j)

    if type == 2:
        i = query[1]
        print(" ".join(map(str, box[i])))

    if type == 3:
        i = query[1]
        print(" ".join(map(str, card[i])))
