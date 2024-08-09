# http://poj.org/problem?id=2386

H, W = map(int, input().split())
B = [input() for _ in range(H)]
V = [[False] * W for _ in range(H)]


def dfs(i, j):
    V[i][j] = True

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and not V[ni][nj] and B[ni][nj] == "W":
            dfs(ni, nj)


ans = 0
for i in range(H):
    for j in range(W):
        if B[i][j] == "W" and not V[i][j]:
            dfs(i, j)
            ans += 1

print(ans)
