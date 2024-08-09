# https://atcoder.jp/contests/atc001/submissions/me

import sys

sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
board = [input() for _ in range(H)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()


def stack_dfs(i, j):
    visited.add((i, j))
    stack = [(i, j)]

    while stack:
        i, j = stack.pop()
        for di, dj in dir:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < H
                and 0 <= nj < W
                and (ni, nj) not in visited
                and board[ni][nj] != "#"
            ):
                visited.add((ni, nj))
                stack.append((ni, nj))


def rec_dfs(i, j):
    visited.add((i, j))

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if (
            0 <= ni < H
            and 0 <= nj < W
            and (ni, nj) not in visited
            and board[ni][nj] != "#"
        ):
            rec_dfs(ni, nj)


start_i, start_j = next(
    (i, j) for i in range(H) for j in range(W) if board[i][j] == "s"
)
goal_i, goal_j = next((i, j) for i in range(H) for j in range(W) if board[i][j] == "g")

# rec_dfs(start_i, start_j)
stack_dfs(start_i, start_j)
print("Yes" if (goal_i, goal_j) in visited else "No")
