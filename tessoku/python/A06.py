from itertools import accumulate

n, q = map(int, input().split())
a = list(map(int, input().split()))

s = [0] + list(accumulate(a))

for _ in range(q):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])

