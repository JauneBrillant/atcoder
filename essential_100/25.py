def dfs(i, j, visited):
    visited.add((i, j))
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for di, dj in direction:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w:
            if (ni, nj) not in visited and grid[ni][nj] == 1:
                dfs(ni, nj, visited)


def solve(grid, h, w):
    island_cnt = 0
    visited = set()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and (i, j) not in visited:
                dfs(i, j, visited)
                island_cnt += 1
    return island_cnt


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]

    print(solve(grid, h, w))
