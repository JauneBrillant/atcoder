import sys

sys.setrecursionlimit(100000)

n, x = map(int, input().split())
ab = []
for _ in range(n):
    ai, bi = map(int, input().split())
    ab.append((ai, bi))
memo = {}


def solve(i=0, pos=0):
    if i == n:
        return pos == x

    if (i, pos) in memo:
        return memo[(i, pos)]

    a, b = ab[i]
    res = solve(i + 1, pos + a) or solve(i + 1, pos + b)
    memo[(i, pos)] = res

    return res


print("Yes" if solve() else "No")
