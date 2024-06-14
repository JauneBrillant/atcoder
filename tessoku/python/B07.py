from itertools import accumulate

t = int(input())
n = int(input())

times = [0] * (t + 1)
for _ in range(n):
    l, r = map(int, input().split())
    times[l] += 1
    times[r] -= 1

acc = list(accumulate(times))

for i in range(t):
    print(acc[i])
