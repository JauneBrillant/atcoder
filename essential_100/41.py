D, N = map(int, input().split())
T = [0]  # 気温
A = []  # 服の適正気温 from
B = []  # 服の適正気温 to
C = []  # 服の派手さ
for _ in range(D):
    T.append(int(input()))
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

# dp[i][j] := i日目に服jをきた時の累計の派手さ
dp = [[-1] * N for _ in range(D + 1)]
for i in range(N):
    if A[i] <= T[1] <= B[i]:
        dp[1][i] = 0

for i in range(2, D + 1):
    for j in range(N):
        if A[j] <= T[i] <= B[j]:  # 服jが選べるなら
            for k in range(N):
                if dp[i - 1][k] != -1:  # 前日着ることができる服限定
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(C[j] - C[k]))

print(max(dp[D]))
