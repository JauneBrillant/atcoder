N, M, Q = map(int, input().split())
questions = list(tuple(map(int, input().split())) for _ in range(Q))


def f(a, seq):
    if len(a) == N:
        seq.append(a.copy())
        return

    last = 1 if len(a) == 0 else a[-1]
    for j in range(last, M + 1):
        a.append(j)
        f(a, seq)
        a.pop()

    return seq


ans = 0
seq = f([], [])
for arr in seq:
    total = 0
    for a, b, c, d in questions:
        a -= 1
        b -= 1
        if arr[b] - arr[a] == c:
            total += d
    ans = max(ans, total)

print(ans)
