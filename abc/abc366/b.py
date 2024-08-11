N = int(input())
S = [input() for _ in range(N)]
M = max(len(s) for s in S)

for i in range(N):
    S[i] += "*" * (M - len(S[i]))

for z in zip(*S):
    print("".join(list(z)[::-1]).rstrip("*"))
