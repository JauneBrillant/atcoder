import sys

sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
C = [input() for _ in range(H)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(i, j, visited, depth):
    visited.add((i, j))

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
            if (ni, nj) == (start_i, start_j) and depth >= 3:
                return True
            if (ni, nj) not in visited and C[ni][nj] == ".":
                res = dfs(ni, nj, visited, depth + 1)
                if res:
                    return True
    return False


start_i, start_j = next((i, j) for i in range(H) for j in range(W) if C[i][j] == "S")
print("Yes" if dfs(start_i, start_j, visited=set(), depth=0) else "No")
