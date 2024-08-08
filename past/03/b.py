N, M, Q = map(int, input().split())

# k: 問題, v:その問題を解いた人
solver = [[] for _ in range(M)]
scores = [0] * N

for _ in range(Q):
    s = list(map(int, input().split()))
    t = s[0]
    n = s[1] - 1

    if t == 1:
        print(scores[n])

    if t == 2:
        m = s[2] - 1
        for i, people in enumerate(solver[m]):
            scores[people] -= 1
        solver[m].append(n)
        scores[n] += N - len(solver[m])
