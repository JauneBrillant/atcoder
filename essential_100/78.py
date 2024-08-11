# from tabulate import tabulate

M, N = map(int, input().split())
K = int(input())
grid = [[" "] * (N + 2) for _ in range(M + 2)]
for i in range(1, M + 1):
    grid[i][1 : N + 1] = input()
pos = []
for _ in range(K):
    a, b, c, d = map(int, input().split())
    pos.append((a, b, c, d))
acc = [[[0] * (3) for _ in range(N + 2)] for _ in range(M + 2)]


# 0 >> ジャングルJ
# 1 >> 海O
# 2 >> 氷I

for i in range(1, M + 1):
    for j in range(1, N + 1):
        acc[i][j][0] += acc[i][j - 1][0]
        acc[i][j][1] += acc[i][j - 1][1]
        acc[i][j][2] += acc[i][j - 1][2]
        if grid[i][j] == "J":
            acc[i][j][0] += 1
        if grid[i][j] == "O":
            acc[i][j][1] += 1
        if grid[i][j] == "I":
            acc[i][j][2] += 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        acc[j][i][0] += acc[j - 1][i][0]
        acc[j][i][1] += acc[j - 1][i][1]
        acc[j][i][2] += acc[j - 1][i][2]

# print(tabulate(grid))
# print(tabulate(acc))

for a, b, c, d in pos:
    cnt_j = acc[a - 1][b - 1][0] + acc[c][d][0] - acc[c][b - 1][0] - acc[a - 1][d][0]
    cnt_o = acc[a - 1][b - 1][1] + acc[c][d][1] - acc[c][b - 1][1] - acc[a - 1][d][1]
    cnt_i = acc[a - 1][b - 1][2] + acc[c][d][2] - acc[c][b - 1][2] - acc[a - 1][d][2]
    print(cnt_j, cnt_o, cnt_i)
