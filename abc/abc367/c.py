# from itertools import product

# N, K = map(int, input().split())
# R = list(map(int, input().split()))

# for p in product(*(range(1, r + 1) for r in R)):
#     if sum(p) % K == 0:
#         print(*p)

N, K = map(int, input().split())
R = list(map(int, input().split()))


def f(a, i):
    if i == N:
        if sum(a) % K == 0:
            print(*a)
        return

    for j in range(1, R[i] + 1):
        a.append(j)
        f(a, i + 1)
        a.pop()


f([], 0)
