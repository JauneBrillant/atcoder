# https://onlinejudge.u-aizu.ac.jp/problems/1160

import sys

sys.setrecursionlimit(10**6)


def dfs(i, j):
    visited[i][j] = True

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and B[ni][nj] == "1":
            dfs(ni, nj)


while True:
    W, H = map(int, input().split())
    if W == H == 0:
        exit()
    B = [input().split() for _ in range(H)]

    visited = [[False] * W for _ in range(H)]
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if B[i][j] == "1" and not visited[i][j]:
                dfs(i, j)
                ans += 1
    print(ans)
