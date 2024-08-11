N = int(input())
S = [input() for _ in range(N)]

# ①  zipを使う
# for z in zip(*S):
#     print("".join(z)[::-1])

# ②  元の行列が、新しい行列のどこに入るかを考える
# M = max(len(s) for s in S)
# T = [["*"] * N for _ in range(M)]
# for i in range(N):
#     for j in range(M):
#         T[j][N - i - 1] = S[i][j]

# for t in T:
#     print("".join(t))

# ③  新しい行列は、元の行列のどこから取ってくるかを考える
M = max(len(s) for s in S)
T = [["*"] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        T[i][j] = S[N - 1 - j][i]

for t in T:
    print("".join(t))
