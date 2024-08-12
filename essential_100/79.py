from itertools import accumulate

N, M, Q = map(int, input().split())
lr = list(tuple(map(int, input().split())) for _ in range(M))
lr.sort()

acc = [[0] * (N + 1) for _ in range(N + 1)]
for l, r in lr:
    acc[l][r] += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        acc[i][j] += acc[i][j - 1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        acc[j][i] += acc[j - 1][i]


for _ in range(Q):
    p, q = map(int, input().split())
    l, r = min(p, q), max(p, q)
    print(acc[r][r] + acc[l - 1][l - 1] - acc[r][l - 1] - acc[l - 1][r])
