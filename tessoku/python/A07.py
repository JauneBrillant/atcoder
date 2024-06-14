from itertools import accumulate

d = int(input())
n = int(input())

days = [0] * (d + 2)
for _ in range(n):
    l, r = map(int, input().split())
    days[l] += 1
    days[r + 1] -= 1

sums = list(accumulate(days))
for i in range(1, d + 1):
    print(sums[i])
