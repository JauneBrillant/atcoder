from copy import deepcopy

H, W = 10, 10
B = [list(input()) for _ in range(H)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(i, j, board, visited):
    visited.add((i, j))

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if (
            0 <= ni < H
            and 0 <= nj < W
            and board[ni][nj] == "o"
            and (ni, nj) not in visited
        ):
            dfs(ni, nj, board, visited)


def try_ok(x, y):
    cnt = 0
    board = deepcopy(B)
    board[x][y] = "o"
    visited = set()

    for i in range(H):
        for j in range(W):
            if board[i][j] == "o" and (i, j) not in visited:
                dfs(i, j, board, visited)
                cnt += 1

    if cnt == 1:
        return True
    else:
        return False


ok = False
for i in range(H):
    for j in range(W):
        if B[i][j] == "x":
            if try_ok(i, j):
                ok = True
                break

print("YES" if ok else "NO")
